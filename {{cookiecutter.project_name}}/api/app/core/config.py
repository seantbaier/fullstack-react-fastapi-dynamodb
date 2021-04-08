from typing import List, Union, Optional
from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    ALLOWED_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("ALLOWED_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # AWS Credentials
    # dynamodb is added at the beginning of these since
    # AWS doesnt allow loambda to have reserved keywords in the vars
    # These will be replaced wit hsuer auth later
    DYNAMODB_AWS_DEFAULT_REGION: Optional[str] = "us-east-1"
    DYNAMODB_AWS_SECRET_ACCESS_KEY: Optional[str]
    DYNAMODB_AWS_ACCESS_KEY_ID: Optional[str]
    DYNAMODB_AWS_ROLE_ARN: Optional[str]
    DYNAMODB_LOCAL_URL: Optional[str] = None

    RUNTIME_ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"
    PROJECT_NAME: str
    USERS_OPEN_REGISTRATION: bool = True
    DEFAULT_QUERY_LIMIT: int = 25
    DEFAULT_QUERY_SORT: str = "created_at"
    DEFAULT_QUERY_SKIP: int = 0

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
