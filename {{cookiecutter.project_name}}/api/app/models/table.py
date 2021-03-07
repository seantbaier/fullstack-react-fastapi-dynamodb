from typing import Optional

from pydantic import BaseModel

from app.core.config import settings


class Key(BaseModel):
    AttributeName: str
    KeyType: str


class AttributeDefinition(BaseModel):
    AttributeName: str
    AttributeType: str


class Table(BaseModel):
    TableName: str
    KeySchema: list
    AttributeDefinitions: list
    ProvisionedThroughput: Optional[dict] = dict(
        {
            "ReadCapacityUnits": settings.READ_CAPACITY_UNITS,
            "WriteCapacityUnits": settings.WRITE_CAPACITY_UNITS,
        }
    )
