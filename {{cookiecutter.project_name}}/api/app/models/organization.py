from typing import Optional
from pydantic import BaseModel
from datetime import datetime


# Shared properties
class Organization(BaseModel):
    id: str
    name: str
