# -----------------------------------------------------------------------------
# Data: Identity
# -----------------------------------------------------------------------------
locals {
  tags = {
    Terraform   = true
    App         = var.app_name
    Environment = var.env
  }
}

# -----------------------------------------------------------------------------
# Resource: Cognito
# -----------------------------------------------------------------------------

resource "aws_cognito_user_pool" "this" {
  name                     = "${var.env}-${var.app_name}-user-pool"
  username_attributes      = ["email"]
  auto_verified_attributes = ["email"]

  verification_message_template {
    default_email_option  = "CONFIRM_WITH_LINK"
    email_message_by_link = "Click the link to confirm your email address {##Click Here##}"
    email_subject_by_link = "Please confirm your email address."
  }

  account_recovery_setting {
    recovery_mechanism {
      name     = "verified_email"
      priority = 1
    }
  }

  admin_create_user_config {
    allow_admin_create_user_only = false
  }

  password_policy {
    minimum_length                   = 8
    require_lowercase                = true
    require_numbers                  = true
    require_symbols                  = true
    require_uppercase                = true
    temporary_password_validity_days = 7
  }

  username_configuration {
    case_sensitive = false
  }

  schema {
    name                     = "email"
    attribute_data_type      = "String"
    developer_only_attribute = false
    mutable                  = false
    required                 = true


    string_attribute_constraints {
      min_length = 7
      max_length = 35
    }
  }


  tags = local.tags

}

resource "aws_cognito_user_pool_client" "this" {
  name          = "${var.env}-${var.app_name}-user-pool-client"
  user_pool_id  = aws_cognito_user_pool.this.id
  callback_urls = ["http://localhost:3000", "https://${var.env}.${var.domain_name}"]
  logout_urls   = ["http://localhost:3000", "https://${var.env}.${var.domain_name}"]
  # generate_secret                      = true
  allowed_oauth_flows_user_pool_client = true
  supported_identity_providers         = ["COGNITO", "Google", ]
  allowed_oauth_flows                  = ["code"]
  allowed_oauth_scopes                 = ["phone", "email", "openid", "profile", "aws.cognito.signin.user.admin"]
  read_attributes                      = ["email", "given_name", "family_name"]
  refresh_token_validity               = 7
}

resource "aws_cognito_user_pool_domain" "this" {
  domain          = "${var.env}-auth.${var.domain_name}"
  certificate_arn = var.certificate_arn
  user_pool_id    = aws_cognito_user_pool.this.id
}

resource "aws_cognito_user_group" "users" {
  name         = "users"
  user_pool_id = aws_cognito_user_pool.this.id
  description  = "Regular users, non-admins"
}

resource "aws_cognito_user_group" "admin_users" {
  name         = "admins"
  user_pool_id = aws_cognito_user_pool.this.id
  description  = "Admin user group"
}


resource "aws_cognito_identity_provider" "google" {
  user_pool_id  = aws_cognito_user_pool.this.id
  provider_name = "Google"
  provider_type = "Google"

  provider_details = {
    authorize_scopes = "email"
    client_id        = var.google_client_id
    client_secret    = var.google_client_secret
  }

  attribute_mapping = {
    email       = "email"
    family_name = "family_name"
    given_name  = "given_name"
    picture     = "picture"
  }
}

resource "aws_cognito_identity_pool" "this" {
  identity_pool_name               = "${var.env}-${var.app_name}-identity-pool"
  allow_unauthenticated_identities = false

  cognito_identity_providers {
    client_id               = aws_cognito_user_pool_client.this.id
    provider_name           = "cognito-idp.us-east-1.amazonaws.com/${aws_cognito_user_pool.this.id}"
    server_side_token_check = true
  }

  # cognito_identity_providers {
  #   client_id               = aws_cognito_user_pool_client.this.id
  #   provider_name           = aws_cognito_identity_provider.google.provider_name
  #   server_side_token_check = false
  # }

  supported_login_providers = {
    "accounts.google.com" = var.google_client_id
  }
}


# -----------------------------------------------------------------------------
# Data: Route53
# -----------------------------------------------------------------------------

data "aws_route53_zone" "this" {
  name = var.domain_name
}

# -----------------------------------------------------------------------------
# Resources: Route53
# -----------------------------------------------------------------------------

# This record is so Cognito custom domain can be used.
resource "aws_route53_record" "root_alias" {
  name    = var.domain_name
  type    = "A"
  zone_id = data.aws_route53_zone.this.zone_id
  ttl     = 300
  records = ["127.0.0.1"]
}

resource "aws_route53_record" "auth_cognito_A" {
  name    = aws_cognito_user_pool_domain.this.domain
  type    = "A"
  zone_id = data.aws_route53_zone.this.zone_id

  alias {
    evaluate_target_health = false
    name                   = aws_cognito_user_pool_domain.this.cloudfront_distribution_arn

    # This is always the user pool custom domain cloudfront.zone_id
    zone_id = "Z2FDTNDATAQYW2"
  }
}
