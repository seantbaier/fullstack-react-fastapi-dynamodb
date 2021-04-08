import boto3
from boto3.dynamodb.conditions import Key
from fastapi.encoders import jsonable_encoder
from fastapi import status
from typing import List
from uuid import uuid4
from botocore.exceptions import ClientError
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from app.crud.base import CRUDBase
from app.models import Project
from app.schemas.project import ProjectCreate, ProjectUpdate
from app.utils.dynamodb import format_items_response, format_item_response
from app.api.deps import get_db


class CRUDProject(CRUDBase[Project, ProjectCreate, ProjectUpdate]):
    def get_by_id(self, dynamodb=None, *, project_id: str) -> Project:
        if not dynamodb:
            dynamodb = get_db()

        db = dynamodb.get_resource()
        table = db.Table("projects")

        try:
            response = table.get_item(Key={"id": project_id})
            return format_item_response(response)
        except Exception as e:
            raise e

    def get_multi(self, dynamodb=None, *, limit: int = 15) -> List[Project]:
        if not dynamodb:
            dynamodb = get_db()

        try:
            db = dynamodb.get_resource()
            table = db.Table("projects")
            response = table.scan(Limit=limit)

            return format_items_response(response)
        except Exception as e:
            raise e

    def create(self, dynamodb=None, *, obj_in: ProjectCreate) -> Project:
        if not dynamodb:
            dynamodb = get_db()

        db = dynamodb.get_resource()

        table = db.Table("projects")
        obj_in_data = jsonable_encoder(obj_in)

        id = str(uuid4())
        db_obj = self.model(**obj_in_data, id=id)

        response = table.put_item(Item=dict(db_obj))

        if "ResponseMetadata" in response:
            meta_data = response["ResponseMetadata"]
            if "HTTPStatusCode" in meta_data:
                if meta_data["HTTPStatusCode"] == 200:
                    expense = table.get_item(Key={"id": id})
                    return Project(**expense["Item"])
        raise HTTPException(status_code=400, detail="Bad Request")

    def update(self, dynamodb=None, *, obj_in: ProjectUpdate) -> Project:
        if not dynamodb:
            dynamodb = get_db()

        db = dynamodb.get_resource()
        table = db.Table("projects")

        obj_in_data = jsonable_encoder(obj_in)
        id = obj_in_data["id"]
        existing_expense = table.get_item(Key={"id": id})

        if not existing_expense:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Could not find expense={id}",
            )

        if not "Item" in existing_expense:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Could not find expense={id}",
            )

        keys_to_update = []
        for key in obj_in_data.keys():
            if not key == "id":
                keys_to_update.append(key)

        update_expression = "set"
        expression_attribute_values = dict()

        for key in keys_to_update:
            index = keys_to_update.index(key)
            update_expression += f" {key}=:{index}"
            expression_attribute_values[f":{index}"] = obj_in_data[key]

            if index < len(keys_to_update) - 1:
                update_expression += ","

        response = table.update_item(
            Key={"id": id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues="ALL_NEW",
        )

        if self.is_successful(response):
            expense = table.get_item(Key={"id": id})
            return Project(**expense["Item"])

        raise HTTPException(status_code=400, detail="Bad Request")

    def delete(self, dynamodb=None, *, project_id: str) -> None:
        if not dynamodb:
            dynamodb = get_db()

        db = dynamodb.get_resource()
        table = db.Table("projects")

        try:
            response = table.delete_item(
                Key={
                    "id": project_id,
                }
            )
        except ClientError as e:
            raise e
        else:
            return response

    def is_successful(self, response):
        if "ResponseMetadata" in response:
            meta_data = response["ResponseMetadata"]
            if "HTTPStatusCode" in meta_data:
                if meta_data["HTTPStatusCode"] == 200:
                    return True

        return False


project = CRUDProject(Project)
