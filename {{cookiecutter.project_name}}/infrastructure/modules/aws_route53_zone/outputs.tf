# Output variable definitions
output "zone_id" {
  description = "Id for the created route53 zone."
  value       = aws_route53_zone.this.zone_id
}