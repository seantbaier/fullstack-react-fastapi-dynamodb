terraform {
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "{{cookiecutter.project_name}}"

    workspaces {
      name = "{{cookiecutter.project_name}}-infrastructure"
    }
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.32"
    }
    local = {
      source  = "hashicorp/local"
      version = "~> 2.1.0"
    }
    template = {
      source  = "hashicorp/template"
      version = "~> 2.2.0"
    }
  }
}

provider "aws" {
  region = var.region
}

# -----------------------------------------------------------------------------
# Resources: IAM
# -----------------------------------------------------------------------------

module "aws_iam_user_circleci" {
  source = "./modules/aws_iam/iam_user"

  user_name                = "${var.app_name}-circleci-user"
  app_name                 = var.app_name
  role_name                = "circleci"
  api_lambda_s3_bucket_arn = module.api.api_lambda_s3_bucket_arn
  api_lambda_function_arn  = module.api.api_lambda_function_arn
  client_s3_bucket_arn     = module.client.s3_bucket_arn
}


# -----------------------------------------------------------------------------
# Identity
# -----------------------------------------------------------------------------


module "identity" {
  source = "./identity"

  env                  = "dev"
  app_name             = var.app_name
  domain_name          = var.domain_name
  certificate_arn      = module.aws_acm_certificate.arn
  google_client_id     = var.dev_google_client_id
  google_client_secret = var.dev_google_client_secret
}

# -----------------------------------------------------------------------------
# DNS
# -----------------------------------------------------------------------------


module "aws_route53_zone" {
  source = "./modules/aws_route53_zone"

  name = var.domain_name
}

# Request new SSL/TLS certificate and validate.
module "aws_acm_certificate" {
  source = "./modules/aws_acm_certificate"

  validate_certificate = true
  wait_for_validation  = false

  zone_id                   = module.aws_route53_zone.zone_id
  subject_alternative_names = ["*.${var.domain_name}"]
  domain_name               = var.domain_name
  validation_method         = "DNS"
  dns_ttl                   = 60
  app_name                  = var.app_name
}

# -----------------------------------------------------------------------------
# Client
# -----------------------------------------------------------------------------


module "client" {
  source = "./client"

  env                 = "dev"
  app_name            = var.app_name
  domain_name         = var.domain_name
  aws_route53_zone_id = module.aws_route53_zone.zone_id
  acm_certificate_arn = module.aws_acm_certificate.arn
}

# -----------------------------------------------------------------------------
# API
# -----------------------------------------------------------------------------


module "api" {
  source = "./api"

  env                    = "dev"
  app_name               = var.app_name
  domain_name            = var.domain_name
  certificate_arn        = module.aws_acm_certificate.arn
  route53_hosted_zone_id = module.aws_route53_zone.zone_id
}


# -----------------------------------------------------------------------------
# Email Service
# -----------------------------------------------------------------------------

# module "email_service" {
#   source = "./email_service"

#   env                    = "dev"
#   app_name               = var.app_name
#   domain_name            = var.domain_name
#   certificate_arn        = module.aws_acm_certificate.arn
#   route53_hosted_zone_id = module.aws_route53_zone.zone_id
# }
