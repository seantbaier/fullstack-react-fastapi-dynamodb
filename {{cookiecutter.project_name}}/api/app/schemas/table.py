"""Using CamelCase on these to match with DynamoDb"""
from typing import List, Optional

from pydantic import BaseModel

from app.core.config import settings


class Key(BaseModel):
    AttributeName: str
    KeyType: str


class AttributeDefinition(BaseModel):
    AttributeName: str
    AttributeType: str


# Shared properties
class TableBase(BaseModel):
    ProvisionedThroughput: Optional[dict] = dict(
        {
            "ReadCapacityUnits": settings.READ_CAPACITY_UNITS,
            "WriteCapacityUnits": settings.WRITE_CAPACITY_UNITS,
        }
    )


# Properties to receive via API on creation
class TableCreate(TableBase):
    TableName: str
    KeySchema: List[Key]
    AttributeDefinitions: List[AttributeDefinition]


class TableUpdate(TableBase):
    TableName: str


class TableOut(BaseModel):
    TableName: str
