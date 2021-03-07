from datetime import datetime
from typing import List, Optional

from pydantic import EmailStr
from pydantic.main import BaseModel


class User(BaseModel):
    id: str
    email: Optional[EmailStr] = None
    hashed_password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: bool = False
    employee_list: Optional[List[str]] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        schema_extra = {
            "example": {
                "email": "steve.rogers@avengers.com",
                "first_name": "steve",
                "last_name": "rogers",
                "is_active": True,
                "employee_list": [],
                "created_at": "2008-09-15T15:53:00+05:00",
                "updated_at": "2008-09-15T15:53:00+05:00",
            }
        }
