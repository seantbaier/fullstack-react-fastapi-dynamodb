output "arn" {
  description = "ARN for the AWS resource."
  value       = aws_iam_role.this[0].arn
}
