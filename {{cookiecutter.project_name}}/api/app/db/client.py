import boto3
from loguru import logger
from uuid import uuid4

from app.core.config import settings


class Session:
    """
    The calls to AWS STS AssumeRole must be signed with the access key ID
    and secret access key of an existing IAM user or by using existing temporary
    credentials such as those from another role. (You cannot call AssumeRole
    with the access key for the root account.) The credentials can be in
    environment variables or in a configuration file and will be discovered
    automatically by the boto3.client() function. For more information, see the
    Python SDK documentation:
    http://boto3.readthedocs.io/en/latest/reference/services/sts.html#client
    """

    def __init__(
        self,
        aws_access_key_id: str = None,
        aws_secret_access_key: str = None,
        session_name: str = None,
    ):
        # create an STS client object that represents a live connection to the
        # STS service
        sts_client = boto3.client(
            "sts",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

        # Call the assume_role method of the STSConnection object and pass the role
        # ARN and a role session name.
        assumed_role_object = sts_client.assume_role(
            RoleArn=settings.DYNAMODB_AWS_ROLE_ARN,
            RoleSessionName=session_name,
        )

        # From the response that contains the assumed role, get the temporary
        # credentials that can be used to make subsequent API calls
        self.credentials = assumed_role_object["Credentials"]
        logger.info(f"Successfully created session={session_name}")


class DynamoDBCLient:
    def __init__(
        self,
        dynamodb_local_url: str = None,
        region_name: str = None,
        aws_access_key_id: str = None,
        aws_secret_access_key: str = None,
    ):
        config = dict(region_name=region_name)

        if (
            settings.RUNTIME_ENVIRONMENT == "local"
            or settings.RUNTIME_ENVIRONMENT == "test"
        ):
            if not dynamodb_local_url:
                logger.error(
                    f"DYNAMODB_URL must be specified if running in ENVIRONMENT={settings.RUNTIME_ENVIRONMENT}"
                )

            config.update(
                endpoint_url=dynamodb_local_url,
                region_name=region_name,
                aws_access_key_id="",
                aws_secret_access_key="",
            )

        else:
            # TODO update session_name to add username when auth is implemented.
            session = Session(
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                session_name=f"AssumeRoleSession_{uuid4()}",
            )

            config.update(
                aws_access_key_id=session.credentials["AccessKeyId"],
                aws_secret_access_key=session.credentials["SecretAccessKey"],
                aws_session_token=session.credentials["SessionToken"],
            )

        self.client = boto3.client("dynamodb", **config)
        logger.info(
            f"Successfully connected to dynamodb:{settings.RUNTIME_ENVIRONMENT}"
        )


dynamodb = DynamoDBCLient(
    dynamodb_local_url=settings.DYNAMODB_LOCAL_URL,
    region_name=settings.DYNAMODB_AWS_DEFAULT_REGION,
    aws_access_key_id=settings.DYNAMODB_AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.DYNAMODB_AWS_SECRET_ACCESS_KEY,
)
