variable "env" {
  description = "Environment the resource is provisioned in."
  type        = string
}

variable "app_name" {
  description = "Application/project name."
  type        = string
}

variable "domain_name" {
  description = "Custom domain name."
  type        = string
}

variable "certificate_arn" {
  description = "ACM arn for SSL"
  type        = string
}

variable "google_client_id" {
  description = "Client id for Google OAuth."
  type        = string
}

variable "google_client_secret" {
  description = "Client secret for Google OAuth."
  type        = string
}
