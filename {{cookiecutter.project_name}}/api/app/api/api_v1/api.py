from fastapi import APIRouter

from .endpoints import auth, expenses, users

router = APIRouter()
router.include_router(auth.router, prefix="/auth", tags=["Auth"])
router.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])

# Authenticated Routes
router.include_router(users.router, prefix="/users", tags=["Users"])
