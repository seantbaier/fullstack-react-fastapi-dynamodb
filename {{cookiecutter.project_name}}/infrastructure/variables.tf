variable "region" {
  description = "Default Region for Resources"
  type        = string
  default     = "us-east-1"
}

variable "stage" {
  description = "Environment to Resources are being Deployed to"
  type        = string
  default     = "dev"
}


variable "app_name" {
  description = "Name of the application/project"
  type        = string
  default     = "example"
}

variable "domain_name" {
  description = "Domain name for application/project"
  type        = string
  default     = "example.com"
}

variable "dev_google_client_id" {
  description = "Client id for Google OAuth."
  type        = string
}

variable "dev_google_client_secret" {
  description = "Client secret for Google OAuth."
  type        = string
}

variable "local" {
  description = "Running terraform from local CLI"
  type        = bool
  default     = false
}
