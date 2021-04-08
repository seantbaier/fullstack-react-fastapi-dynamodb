variable "create" {
  description = "Create resource conditionally."
  type        = bool
  default     = true
}

variable "env" {
  description = "Environment the resource is provisioned in."
  type        = string
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

variable "name" {
  description = "Name for the AWS resource."
  type        = string
}

variable "managed_policy_arns" {
  description = "List of policy ARNs managed by AWS that this role has access to."
  type        = list(string)
  default     = null
}

variable "assume_role_identifiers" {
  description = "List of the identities (users/services) that are trusted to assume this role."
  type        = list(string)
  default     = null
}

variable "assume_role_type" {
  description = "Type of Assume role ex. 'AWS' or 'Service'"
  type        = string
}
