output "aws_iam_user_circleci" {
  description = "IAM AWS User credentials for CICD"
  value = {
    name = module.aws_iam_user_circleci.name
    access_key = {
      aws_access_key_id = module.aws_iam_user_circleci.aws_access_key
    }
  }
}

output "aws_iam_user_api" {
  description = "IAM AWS User credentials for api"
  value       = module.api.aws_iam_user_api
}

output "aws_cognito_credentials" {
  description = "AWS Cognito credentials"
  value = {
    aws_cognito_user_pool_id        = module.identity.aws_cognito_user_pool_id
    aws_cognito_identity_pool_id    = module.identity.aws_cognito_identity_pool_id
    aws_cognito_user_pool_client_id = module.identity.aws_cognito_user_pool_client_id
  }
}
