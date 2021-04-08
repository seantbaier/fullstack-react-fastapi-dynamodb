locals {
  base_tags = {
    App       = var.app_name
    Terraform = true
  }

  tags = merge(local.base_tags, var.tags)
}

resource "aws_iam_user" "this" {
  count = var.create ? 1 : 0

  name = var.user_name
  tags = local.tags
}

resource "aws_iam_access_key" "this" {
  count = var.create ? 1 : 0

  user = aws_iam_user.this[0].name
}

data "aws_iam_policy_document" "circleci" {
  statement {

    actions = [
      "s3:DeleteObject",
      "s3:GetObject",
      "s3:PutObject",
    ]

    effect = "Allow"

    resources = ["${var.api_lambda_s3_bucket_arn}/*", "${var.client_s3_bucket_arn}/*"]
  }

  statement {
    actions = [
      "s3:ListBucket",
    ]

    effect = "Allow"

    resources = [var.client_s3_bucket_arn]
  }

  statement {
    sid = "PermissionsToCreateAndUpdateFunction"

    effect = "Allow"

    actions = [
      "lambda:CreateFunction",
      "lambda:GetFunction",
      "lambda:UpdateFunctionCode"
    ]

    resources = [var.api_lambda_function_arn]
  }
}

resource "aws_iam_user_policy" "circleci" {
  count = var.create ? 1 : 0

  name   = "${var.user_name}-policy"
  user   = aws_iam_user.this[0].name
  policy = data.aws_iam_policy_document.circleci.json
}
