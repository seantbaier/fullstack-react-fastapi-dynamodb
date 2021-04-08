from typing import Optional
from pydantic import BaseModel
from datetime import datetime


# Shared properties
class Project(BaseModel):
    id: str
    title: str
