variable "create" {
  description = "Create resource conditionally."
  type        = bool
  default = true
}

variable "tags" {
  description = "AWS resrouce tags."
  type        = map
  default     = {}
}

variable "domain_name" {
  description = "Domain name for the certifcate."
  type        = string
}

variable "wait_for_validation" {
  description = "Request to wait for validation to succeed."
  type        = bool
}

variable "validate_certificate" {
  description = "Request validation."
  type        = bool
}

variable "subject_alternative_names" {
  description = "List of alternative sub domains to be validated against."
  type        = list
}

variable "validation_method" {
  description = "The type of method used to validate the certificate. DNS or EMAIL"
  type        = string
}

variable "dns_ttl" {
  description = "dns time to live"
  type        = number
}

variable "zone_id" {
  description = "Zone id for the hosted zone that will be validating by DNS"
}

variable "env" {
  description = "Environment the resource is provisioned in."
  type        = string
  default     = "dev"
}

variable "app_name" {
  description = "Application/project name."
  type        = string
}
