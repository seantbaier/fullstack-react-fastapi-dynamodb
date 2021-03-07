from typing import Optional

from pydantic import BaseModel


# Shared properties
class Expense(BaseModel):
    id: str
    payment_status: str = "due"
    expense_name: str
    monthly_payment: Optional[int] = None
    amount_borrowed: Optional[int] = None
    account_balance: Optional[int] = None
    credit_limit: Optional[int] = None
    paycheck: Optional[int] = None
    due_date: Optional[str] = None
    autopay: Optional[bool] = False
    payment_account: Optional[str] = None
    expense_category: Optional[str] = "uncategorized"
