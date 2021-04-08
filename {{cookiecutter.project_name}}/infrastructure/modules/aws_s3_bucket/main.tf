locals {
  base_tags = {
    Envrionment = var.env
    Terraform   = "true"
    Name        = var.bucket
  }

  tags = merge(local.base_tags, var.tags)
}


resource "aws_s3_bucket" "this" {
  count = var.create ? 1 : 0

  force_destroy = true
  bucket        = var.bucket
  acl           = var.acl


  dynamic "website" {
    for_each = length(keys(var.website)) == 0 ? [] : [var.website]

    content {
      index_document           = lookup(website.value, "index_document", null)
      error_document           = lookup(website.value, "error_document", null)
      redirect_all_requests_to = lookup(website.value, "redirect_all_requests_to", null)
      routing_rules            = lookup(website.value, "routing_rules", null)
    }
  }

  tags = local.tags
}
