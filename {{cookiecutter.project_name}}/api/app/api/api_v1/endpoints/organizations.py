import boto3
from typing import Optional, Any
from fastapi import APIRouter

from app import crud, schemas

router = APIRouter()


@router.get("/", response_model=dict)
def read_organizations(name: Optional[str] = None) -> Any:
    """
    Retrieve Organizations
    """
    try:
        options = dict()

        if name:
            options["name"] = name

        expenses = crud.organization.get_multi(**options)
    except Exception as e:
        raise e
    else:
        return expenses


@router.get("/{organization_id}", response_model=schemas.Organization)
def read_organization(organization_id: str) -> Any:
    """
    Retrieve Organization
    """
    try:
        organization = crud.organization.get_by_id(organization_id=organization_id)
    except Exception as e:
        raise e
    else:
        return organization


@router.post("/", response_model=schemas.Organization)
def create_organization(
    organization: schemas.OrganizationCreate,
) -> Any:
    organization = crud.organization.create(obj_in=organization)

    return organization


@router.put("/", response_model=schemas.Organization)
def update_organization(
    organization: schemas.OrganizationUpdate,
) -> Any:
    organization = crud.organization.update(obj_in=organization)

    return organization


@router.delete("/")
def delete_organization(organization_id: str) -> Any:
    response = crud.organization.delete(organization_id=organization_id)
    return response