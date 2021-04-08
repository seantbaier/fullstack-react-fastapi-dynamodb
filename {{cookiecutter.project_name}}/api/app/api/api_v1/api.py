from fastapi import APIRouter

from .endpoints import users, projects, organizations
from .endpoints.dynamodb import tables

router = APIRouter()
# router.include_router(auth.router, prefix="/auth", tags=["Auth"])
router.include_router(projects.router, prefix="/projects", tags=["Projects"])
router.include_router(
    organizations.router, prefix="/organizations", tags=["Organizations"]
)

# DynamoDB Specific Endpoints
router.include_router(tables.router, prefix="/tables", tags=["Tables"])

# Authenticated Routes
router.include_router(users.router, prefix="/users", tags=["Users"])