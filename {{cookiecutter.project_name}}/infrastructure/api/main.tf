locals {
  base_tags = {
    Terraform   = true
    Environment = var.env
    App         = var.app_name
  }
}


# -----------------------------------------------------------------------------
# IAM User to assume role that allows DynamoDB acess.
# TODO - Once authentiction is in place this will be removed in echange for the logged in users.
# -----------------------------------------------------------------------------

resource "aws_iam_user" "this" {
  name = "${var.env}-${var.app_name}-api-service"

  tags = merge(local.base_tags, {
    Type = "service"
  })
}

resource "aws_iam_access_key" "this" {
  user = aws_iam_user.this.name
}

# -----------------------------------------------------------------------------
# IAM Role that users will assume in a session to get DynamoDB access.
# -----------------------------------------------------------------------------


module "aws_iam_dynamodb_role" {
  source = "../modules/aws_iam/iam_role"

  name                = "${var.env}-${var.app_name}-api-dynamodb-role"
  env                 = var.env
  app_name            = var.app_name
  managed_policy_arns = ["arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess"]
  # This will need to be updated to be a wildcard accepting certain users based off
  # of a key in the arn instead.
  assume_role_type        = "AWS"
  assume_role_identifiers = [aws_iam_user.this.arn]
}

# -----------------------------------------------------------------------------
# S3 bucket that holds the packaged lambda function.zip file.
# -----------------------------------------------------------------------------



module "api_lambda_s3_bucket" {
  source = "../modules/aws_s3_bucket"

  env    = var.env
  bucket = "${var.env}-${var.app_name}-api"
  acl    = "private"
}

# -----------------------------------------------------------------------------
# Lambda function that handles all requests to the API Gateway
# -----------------------------------------------------------------------------


module "aws_lambda_function" {
  source        = "../modules/aws_lambda"
  function_name = "${var.env}-${var.app_name}-api"

  env                   = var.env
  s3_key                = "function.zip"
  lambda_version        = "v1.0.0"
  s3_bucket             = module.api_lambda_s3_bucket.bucket
  aws_dynamodb_role_arn = module.aws_iam_dynamodb_role.arn
  aws_access_key_id     = aws_iam_access_key.this.id
  aws_secret_access_key = aws_iam_access_key.this.secret
  aws_default_region    = "us-east-1"
  runtime               = "python3.8"
  runtime_environment   = "production"
}

# -----------------------------------------------------------------------------
# HTTP Api Gateway that handles all requests and invokes the Lambda
# -----------------------------------------------------------------------------


module "aws_apigatewayv2_api" {
  source = "../modules/aws_http_api_gateway"

  # HTTP API Gateway
  name          = "${var.env}-${var.app_name}-api"
  env           = var.env
  app_name      = var.app_name
  protocol_type = "HTTP"

  # Integration
  integration_type       = "AWS_PROXY"
  integration_method     = "POST"
  integration_uri        = module.aws_lambda_function.arn
  payload_format_version = "2.0"

  # Custom Domain Name
  domain_name     = "${var.env}-api.${var.domain_name}"
  certificate_arn = var.certificate_arn
  endpoint_type   = "REGIONAL"
  security_policy = "TLS_1_2"
}

# Permission to allow API Gateway to invoke lambda.
resource "aws_lambda_permission" "this" {

  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = module.aws_lambda_function.function_name
  principal     = "apigateway.amazonaws.com"

  # The "/*/*" portion grants access from any method on any resource
  # within the API Gateway REST API.
  source_arn = "${module.aws_apigatewayv2_api.execution_arn}/*/*"
}

resource "aws_route53_record" "ipv4" {
  name    = module.aws_apigatewayv2_api.custom_domain_name
  type    = "A"
  zone_id = var.route53_hosted_zone_id

  alias {
    name                   = module.aws_apigatewayv2_api.target_domain_name
    zone_id                = module.aws_apigatewayv2_api.domain_name_hosted_zone_id
    evaluate_target_health = false
  }
}

resource "aws_route53_record" "ipv6" {
  name    = module.aws_apigatewayv2_api.custom_domain_name
  type    = "AAAA"
  zone_id = var.route53_hosted_zone_id

  alias {
    name                   = module.aws_apigatewayv2_api.target_domain_name
    zone_id                = module.aws_apigatewayv2_api.domain_name_hosted_zone_id
    evaluate_target_health = false
  }
}
