import boto3
from typing import Optional, Any
from fastapi import APIRouter

from app import crud, schemas, models

router = APIRouter()


@router.get("/", response_model=dict)
def read_projects(title: Optional[str] = None) -> Any:
    """
    Retrieve Projects
    """
    try:
        options = dict()

        if title:
            options["title"] = title

        expenses = crud.project.get_multi(**options)
    except Exception as e:
        raise e
    else:
        return expenses


@router.get("/{project_id}", response_model=schemas.Project)
def read_project(project_id: str) -> Any:
    """
    Retrieve Project
    """
    try:
        project = crud.project.get_by_id(project_id=project_id)
    except Exception as e:
        raise e
    else:
        return project


@router.post("/", response_model=schemas.Project)
def create_project(
    project: schemas.ProjectCreate,
) -> Any:
    project = crud.project.create(obj_in=project)

    return project


@router.put("/", response_model=schemas.Project)
def update_project(
    project: schemas.ProjectUpdate,
) -> Any:
    project = crud.project.update(obj_in=project)

    return project


@router.delete("/")
def delete_project(project_id: str) -> Any:
    response = crud.project.delete(project_id=project_id)
    return response