variable "env" {
  description = "Environment the resource is provisioned in."
  type        = string
}

variable "app_name" {
  description = "Application/project name."
  type        = string
}

variable "domain_name" {
  description = "Application/project domain name."
  type        = string
}


variable "aws_route53_zone_id" {
  description = "Hosted zone id for domain."
  type        = string
}

variable "acm_certificate_arn" {
  description = "The ARN of the AWS Certificate Manager certificate that you wish to use with this distribution. Specify this, cloudfront_default_certificate, or iam_certificate_id. The ACM certificate must be in US-EAST-1."
  type        = string
  default     = null
}
