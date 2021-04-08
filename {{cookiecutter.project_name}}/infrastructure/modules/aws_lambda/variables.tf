variable "env" {
  description = "Name of the environment the resources are being deployed to."
  type        = string
  default     = "dev"
}

variable "runtime_environment" {
  description = "The runtime environment the lambda is executed in."
  type        = string
  default     = "production"
}

variable "runtime" {
  description = "The runtime of the lambda image."
  type        = string
}

variable "create" {
  description = "Create resource or not."
  type        = bool
  default     = true
}

variable "s3_bucket" {
  description = "S3 Bucket for lambda.zip to be uploade too."
  type        = string
}
variable "lambda_version" {
  description = "Lambda version."
  type        = string
}

variable "s3_key" {
  description = "Filename of the zipped function."
  type        = string
  default     = "function.zip"
}

variable "function_name" {
  description = "Name of function"
  type        = string
}

variable "aws_dynamodb_role_arn" {
  description = "The role that allows the app running on the lambda to access dynamodb."
  type        = string
}

variable "aws_access_key_id" {
  description = "This will be removed once auth is done"
  type        = string
}

variable "aws_secret_access_key" {
  description = "This will be removed once auth is done"
  type        = string
}

variable "aws_default_region" {
  description = "This will be removed once auth is done"
  type        = string
}

