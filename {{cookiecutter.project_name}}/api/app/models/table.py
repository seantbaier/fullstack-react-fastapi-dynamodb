from typing import Optional, List
from pydantic import BaseModel

from app.core.config import settings

READ_CAPACITY_UNITS = 10
WRITE_CAPACITY_UNITS = 10


class Key(BaseModel):
    AttributeName: str
    KeyType: str


class AttributeDefinition(BaseModel):
    AttributeName: str
    AttributeType: str


class Table(BaseModel):
    TableName: str
    KeySchema: List[Key]
    AttributeDefinitions: List[AttributeDefinition]
    BillingMode: str = "PAY_PER_REQUEST"
