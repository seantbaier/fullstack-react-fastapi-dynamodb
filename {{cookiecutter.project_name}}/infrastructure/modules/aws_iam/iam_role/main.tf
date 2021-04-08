locals {
  base_tags = {
    Environment = var.env
    Terraform   = true
    App         = var.app_name
  }

  tags = merge(local.base_tags, var.tags)
}

resource "aws_iam_role" "this" {
  count = var.create ? 1 : 0

  name                = var.name
  managed_policy_arns = var.managed_policy_arns
  assume_role_policy  = data.aws_iam_policy_document.this.json
}

data "aws_iam_policy_document" "this" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = var.assume_role_type
      identifiers = var.assume_role_identifiers
    }
  }
}
