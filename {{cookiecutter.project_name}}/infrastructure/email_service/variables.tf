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

variable "certificate_arn" {
  description = "ACM arn for SSL"
  type        = string
}

variable "route53_hosted_zone_id" {
  description = "Zone Id for the application common hosted zone."
  type        = string
}


