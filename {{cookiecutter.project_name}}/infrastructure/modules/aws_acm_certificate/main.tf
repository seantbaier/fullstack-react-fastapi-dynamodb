locals {
  # Get distinct list of domains and SANs
  distinct_domain_names = distinct(
    [for s in concat([var.domain_name], var.subject_alternative_names) : replace(s, "*.", "")]
  )

  # Copy domain_validation_options for the distinct domain names
  validation_domains = var.create ? [for k, v in aws_acm_certificate.this[0].domain_validation_options : tomap(v) if contains(local.distinct_domain_names, replace(v.domain_name, "*.", ""))] : []

  base_tags = {
    App       = var.app_name
    Terraform = true
  }

  tags = merge(local.base_tags, var.tags)
}

resource "aws_acm_certificate" "this" {
  count = var.create ? 1 : 0

  domain_name               = var.domain_name
  subject_alternative_names = var.subject_alternative_names
  validation_method         = var.validation_method

  tags = local.tags

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_route53_record" "validation" {
  count = var.create && var.validation_method == "DNS" && var.validate_certificate ? length(local.distinct_domain_names) : 0

  zone_id         = var.zone_id
  name            = element(local.validation_domains, count.index)["resource_record_name"]
  type            = element(local.validation_domains, count.index)["resource_record_type"]
  ttl             = var.dns_ttl
  allow_overwrite = true

  records = [
    element(local.validation_domains, count.index)["resource_record_value"]
  ]

  depends_on = [aws_acm_certificate.this]
}

resource "aws_acm_certificate_validation" "this" {
  count                   = var.create && var.validation_method == "DNS" && var.validate_certificate && var.wait_for_validation ? 1 : 0
  
  certificate_arn         = aws_acm_certificate.this[0].arn
  validation_record_fqdns = aws_route53_record.validation.*.fqdn
}
