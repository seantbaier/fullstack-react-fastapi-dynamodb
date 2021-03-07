from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str
    ALGORITHM: str
    # SECRET_KEY: str = secrets.token_urlsafe(31)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
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
    AWS_SECRET_ACCESS_KEY: str
    AWS_ACCESS_KEY: str
    AWS_DEFAULT_REGION: str

    # Database
    DYNAMODB_URL: str
    READ_CAPACITY_UNITS: int
    WRITE_CAPACITY_UNITS: int

    PROJECT_NAME: str
    USERS_OPEN_REGISTRATION: bool = True
    DEFAULT_QUERY_LIMIT: int = 25
    DEFAULT_QUERY_SORT: str = "created_at"
    DEFAULT_QUERY_SKIP: int = 0

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
