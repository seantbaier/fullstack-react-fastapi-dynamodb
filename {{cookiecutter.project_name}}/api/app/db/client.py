import boto3

from app.core.config import settings


class DynamoDBCLient:
    def __init__(self):
        # config = dict(endpoint_url=settings.DYNAMODB_URL)
        config = dict(region_name=settings.AWS_DEFAULT_REGION)

        self.client = boto3.client("dynamodb", **config)
        self.resource = boto3.resource("dynamodb", **config)

    def get_client(self):
        return self.client

    def get_resource(self):
        return self.resource
