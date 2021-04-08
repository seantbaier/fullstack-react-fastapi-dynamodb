######################################################
# Client
######################################################

locals {
  client_s3_bucket_name = "${var.env}-${var.domain_name}"
}


module "client_s3_bucket" {
  source = "../modules/aws_s3_bucket"


  env    = "dev"
  bucket = local.client_s3_bucket_name

  acl                     = "public-read"
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false

  website = {
    index_document = "index.html"
    error_document = "index.html"
  }
}

module "aws_cloudfront_distribution" {
  source = "../modules/aws_cloudfront_distribution"

  env                 = var.env
  app_name            = var.app_name
  aliases             = ["${var.env}.${var.domain_name}"]
  acm_certificate_arn = var.acm_certificate_arn

  aws_s3_bucket_origin = {
    arn                         = module.client_s3_bucket.arn
    id                          = module.client_s3_bucket.id
    bucket_regional_domain_name = module.client_s3_bucket.bucket_regional_domain_name
  }
}

resource "aws_route53_record" "ipv4" {
  name    = "${var.env}.${var.domain_name}"
  type    = "A"
  zone_id = var.aws_route53_zone_id

  alias {
    evaluate_target_health = true
    name                   = module.aws_cloudfront_distribution.domain_name
    zone_id                = module.aws_cloudfront_distribution.hosted_zone_id
  }
}

resource "aws_route53_record" "ipv6" {
  name    = "${var.env}.${var.domain_name}"
  type    = "AAAA"
  zone_id = var.aws_route53_zone_id

  alias {
    evaluate_target_health = true
    name                   = module.aws_cloudfront_distribution.domain_name
    zone_id                = module.aws_cloudfront_distribution.hosted_zone_id
  }
}
