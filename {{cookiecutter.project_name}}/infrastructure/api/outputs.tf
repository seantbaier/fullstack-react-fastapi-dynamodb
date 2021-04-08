output "api_lambda_s3_bucket_arn" {
  description = "S3 bucket ARN for the lambda s3 bucket."
  value       = module.api_lambda_s3_bucket.arn
}

output "api_lambda_function_arn" {
  description = "ARN for the main proxy lambda function."
  value       = module.aws_lambda_function.arn
}

output "aws_iam_user_api_access_key" {
  description = "AWS secret access key and access key id."
  value = {
    aws_access_key_id     = aws_iam_access_key.this.id
    aws_secret_access_key = aws_iam_access_key.this.secret
  }
}

output "aws_iam_user_api" {
  description = "AWS secret access key and access key id."
  value = {
    name                  = aws_iam_user.this.name
    aws_access_key_id     = aws_iam_access_key.this.id
    aws_secret_access_key = aws_iam_access_key.this.secret
  }
}
