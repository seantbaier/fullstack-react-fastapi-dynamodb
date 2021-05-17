"""Using CamelCase on these to match with DynamoDb"""
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel


class Tag(BaseModel):
    Key: str
    Value: str


class KeyType(str, Enum):
    hash = "HASH"
    range = "RANGE"


class ProjectionType(str, Enum):
    all = "ALL"
    keys_only = "KEYS_ONLY"
    include = "INCLUDE"


class KeySchema(BaseModel):
    AttributeName: str
    KeyType: KeyType


class AttributeDefinition(BaseModel):
    AttributeName: str = "attribute_definition"
    AttributeType: str = "S"


class Projection(BaseModel):
    ProjectionType: ProjectionType
    NonKeyAttributes: List[str]


class Create(BaseModel):
    IndexName: str
    BillingMode: str = "PAY_PER_REQUEST"


class Update(BaseModel):
    IndexName: str
    BillingMode: str = "PAY_PER_REQUEST"


# Shared properties
class TableBase(BaseModel):
    TableName: str


# Properties to receive via API on creation
class TableCreate(TableBase):
    KeySchema: List[KeySchema]
    AttributeDefinitions: List[AttributeDefinition]
    BillingMode: str = "PAY_PER_REQUEST"
    Tags: Optional[List[Tag]]

    class Config:
        schema_extra = {
            "example": {
                "TableName": "new_table",
                "KeySchema": [
                    {"AttributeName": "index_key", "KeyType": "HASH"},
                    {"AttributeName": "sort_key", "KeyType": "RANGE"},
                ],
                "AttributeDefinitions": [
                    {"AttributeName": "index_key", "AttributeType": "S"},
                    {"AttributeName": "sort_key", "AttributeType": "S"},
                ],
                "BillingMode": "PAY_PER_REQUEST",
                "Tags": [{"Key": "tag_name", "Value": "tag_value"}],
            }
        }


class TableUpdate(BaseModel):
    TableName: str
    AttributeDefinitions: List[AttributeDefinition]


class TableOut(BaseModel):
    TableName: str
    KeySchema: List[KeySchema]
    AttributeDefinitions: List[AttributeDefinition]
    TableStatus: str
    ItemCount: Optional[int]
