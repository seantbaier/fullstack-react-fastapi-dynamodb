output "name" {
  description = "IAM User name"
  value       = aws_iam_user.this[0].name
}

output "aws_access_key" {
  description = "AWS secret access key and access key id."
  value = {
    aws_access_key_id     = aws_iam_access_key.this[0].id
    aws_secret_access_key = aws_iam_access_key.this[0].secret
  }
}
