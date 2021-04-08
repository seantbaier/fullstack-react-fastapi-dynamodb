# Create
variable "create" {
  description = "Create resource conditionally."
  type        = bool
  default     = true
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

variable "tags" {
  description = "AWS resrouce tags."
  type        = map
  default     = {}
}


variable "api_lambda_s3_bucket_arn" {
  description = "ARN for the s3 Bucket user needs permissions to."
  type        = string
}

variable "client_s3_bucket_arn" {
  description = "ARN for the s3 Bucket user needs permissions to."
  type        = string
}

variable "api_lambda_function_arn" {
  description = "ARN for the lambda that the user needs permissiosn to."
  type        = string
}

variable "role_name" {
  description = "IAM role name"
  type        = string
  default     = ""
}

variable "user_name" {
  description = "Desired name for the IAM user"
  type        = string
}
