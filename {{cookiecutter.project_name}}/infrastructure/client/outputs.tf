output "s3_bucket_arn" {
  description = "ARN for the static webstie S3 bucket."
  value       = module.client_s3_bucket.arn
}
