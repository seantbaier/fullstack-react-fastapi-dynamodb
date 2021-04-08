resource "aws_ses_email_identity" "this" {
  email = "info@${var.domain_name}"
}

resource "aws_ses_domain_identity" "this" {
  domain = var.domain_name
}

resource "aws_route53_record" "amazonses_verification_record" {
  zone_id = var.route53_hosted_zone_id
  name    = "_amazonses.${aws_ses_domain_identity.this.id}"
  type    = "TXT"
  ttl     = "600"
  records = [aws_ses_domain_identity.this.verification_token]
}

# Does not create any AWS resources just for Terraform to manage workflow.
resource "aws_ses_domain_identity_verification" "verification" {
  domain = aws_ses_domain_identity.this.id

  depends_on = [aws_route53_record.amazonses_verification_record]
}

# Add DKIM
resource "aws_ses_domain_dkim" "this" {
  domain = aws_ses_domain_identity.this.domain
}

# verify DKIM
resource "aws_route53_record" "this" {
  count   = 3
  zone_id = var.route53_hosted_zone_id
  name    = "${element(aws_ses_domain_dkim.this.dkim_tokens, count.index)}._domainkey"
  type    = "CNAME"
  ttl     = "600"
  records = ["${element(aws_ses_domain_dkim.this.dkim_tokens, count.index)}.dkim.amazonses.com"]
}

# Workmail

# Create SMTP User
# Create SMTP Credentials for User

# Port
# Server

# alarm for reputation
