"""Using CamelCase on these to match with DynamoDb"""
from typing import Optional

from pydantic import BaseModel


# Shared properties
class ExpenseBase(BaseModel):
    payment_status: Optional[str] = None
    expense_name: Optional[str] = None
    monthly_payment: Optional[int] = None
    amount_borrowed: Optional[int] = None
    account_balance: Optional[int] = None
    credit_limit: Optional[int] = None
    percent_used: Optional[int] = None
    paycheck: Optional[int] = None
    due_date: Optional[str] = None
    autopay: Optional[bool] = False
    payment_account: Optional[str] = None
    expense_category: Optional[str] = "uncategorized"


# Properties to receive on item creation
class ExpenseCreate(ExpenseBase):
    payment_status: str
    expense_name: str


# Properties to receive on item update
class ExpenseUpdate(ExpenseBase):
    id: str
    pass


# Properties shared by models stored in DB
class ExpenseInDBBase(ExpenseBase):
    id: str
    expense_name: str


# Properties to return to client
class Expense(ExpenseInDBBase):
    pass


# Properties properties stored in DB
class ExpenseInDB(ExpenseInDBBase):
    pass
