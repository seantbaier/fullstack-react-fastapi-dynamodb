output "aws_cognito_user_pool_id" {
  description = "AWS Cognito user pool id"
  value       = aws_cognito_user_pool.this.id
}

output "aws_cognito_identity_pool_id" {
  description = "AWS Cognito identity pool id"
  value       = aws_cognito_identity_pool.this.id
}

output "aws_cognito_user_pool_client_id" {
  description = "AWS Cognito user pool client id"
  value       = aws_cognito_user_pool_client.this.id
}
