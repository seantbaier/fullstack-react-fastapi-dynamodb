from typing import Any, Optional

from fastapi import APIRouter

from app import crud, schemas

router = APIRouter()


@router.get("/", response_model=dict)
def read_expenses(expense_category: Optional[str] = None) -> Any:
    """
    Retrieve Expenses
    """
    try:
        options = dict()

        if expense_category:
            options["expense_category"] = expense_category

        expenses = crud.expense.get_multi(**options)
    except Exception as e:
        raise e
    else:
        return expenses


@router.get("/{expense_id}", response_model=schemas.Expense)
def read_expense(expense_id: str) -> Any:
    """
    Retrieve Expense
    """
    try:
        expense = crud.expense.get_by_id(expense_id=expense_id)
    except Exception as e:
        raise e
    else:
        return expense


@router.post("/", response_model=schemas.Expense)
def create_expense(
    expense_item: schemas.ExpenseCreate,
) -> Any:
    expense = crud.expense.create(obj_in=expense_item)

    return expense


@router.put("/", response_model=schemas.Expense)
def update_expense(
    expense_item: schemas.ExpenseUpdate,
) -> Any:
    expense = crud.expense.update(obj_in=expense_item)

    return expense


@router.delete("/")
def delete_expense(expense_id: str) -> Any:
    response = crud.expense.delete(expense_id=expense_id)
    return response
