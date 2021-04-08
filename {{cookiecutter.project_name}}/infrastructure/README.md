# FastApi Serverless Infrastructure

```markdown
## TODO

1. Bootstrap scripts for spinning up new environments

- Create boiler plate lambda - function.zip
- Create boiler plate react frontend - index.html
- .sh script or Makefile to run the terraform commands depending on new env or existing updates.

2. Add Query log to Hosted Zone

3. Add Billing Arms

4. CICD Access Key

- the IAM User provisioned for the CICD generates an access key.
- This key either needs to be added to the pipeline somehow or output to a file.
```

## 1. Setup API

1. Setup API Locally
2. Package Lambda Locally
3. Configure AWS CLI
4. Create S3 Bucket and version folder

### upload Lambda
  
```shell
aws s3 cp ../tf-lambda.zip s3://terraform-serverless-example/v1.0.0/example.zip
```

## 2. Setup Terraform

1. Update App name to main.tf
2. Create Terraform Cloud Workspace
3. Add Terraform AWS Credendtials (This is separate from the credentials used in CircleCi)

### Initialize Terraform

```shell
terraform init
```

### Validate

```shell
terraform validate
```

### Plan

```shell
terraform plan
```

### Apply

```shell
terraform apply
```

TODO: API Gateway Stage is still not working correctly have to delete it in AWS console and apply again.

## Setup CircleCi

1. Create new keys for the newly created circleci user
2. Create context for each env
3. add project envs

## Outputs

```shell
terraform output -json > outputs.json
```
