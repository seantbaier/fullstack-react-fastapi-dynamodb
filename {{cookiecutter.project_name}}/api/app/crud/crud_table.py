from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status
from typing import List
from loguru import logger
from pprint import pprint

from starlette.status import HTTP_400_BAD_REQUEST

from app.crud.base import CRUDBase
from app.models import Table
from app.schemas.dynamodb.table import TableBase, TableCreate, TableUpdate, TableOut
from app.api.deps import get_db
from app.utils.errors import handle_error

LIMIT = 15


class CRUDTable(CRUDBase[Table, TableCreate, TableUpdate]):
    def get(self, *, table_name: str) -> List[TableOut]:
        """
        Fetch a table from a given TableName. If table does not exists raise 404 Not Found Error

        Parameters
        - table_name: (string) Name of the table to get

        Returns
        - table - (TableOut)
        """
        try:
            db = get_db()
            response = db.describe_table(TableName=table_name)

            table = response["Table"]
            table_out = TableOut(**table)

            return table_out
        except Exception as e:
            error = handle_error(e)
            raise error

    def get_multi(self, *, exclusive_start_table_name, limit: int = LIMIT) -> List[TableBase]:
        db = get_db()
        options = dict(Limit=limit)

        if exclusive_start_table_name:
            options["ExclusiveStartTableName"] = exclusive_start_table_name

        response = db.list_tables(**options)

        tables = []
        if "TableNames" in response:
            for name in response["TableNames"]:
                tables.append(dict(TableName=name))

        return tables

    def create(self, *, obj_in: TableCreate) -> TableOut:
        """
        Check if the table already exists. If table already exists raise a 400 error.
        If table does not exist create a new table.

        Since `describe_table` raises an exception if the Table does not exist, except the error and create.

        Parameters
        - obj_in: (TableCreate)

        Returns
        - table - (TableOut)
        """
        db = get_db()

        try:
            # Check for existing table. This will raise a 400 ResourceNotFoundException from AWS if the Table does not exist.
            response = db.describe_table(TableName=obj_in.TableName)
            table = response["Table"]

            if table:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail=f"Table: '{obj_in.TableName}' already exists!"
                )
        except (HTTPException, Exception) as e:
            # Format and change status_code to 404
            error = handle_error(e)

            # Since describe_table raises an exception if the Table does not exist
            # excepting creating Table if 404.
            if isinstance(error, HTTPException) and error.status_code == 404:
                obj_in_data = jsonable_encoder(obj_in)
                table = db.create_table(**obj_in_data)

                table_name = table["TableDescription"]["TableName"]

                if table_name == obj_in.TableName:
                    logger.info(f"Successfully created `{table['TableDescription']['TableName']}` dynamodb table.")

                    return TableOut(**table["TableDescription"])
                else:
                    logger.error(f"Something went wrong. {obj_in.TableName} table not created.", table)

            raise error

    def update(self, dynamodb=None, *, obj_in: TableUpdate) -> Table:
        if not dynamodb:
            dynamodb = get_db()

        db = dynamodb.get_client()
        table = db.describe_table(TableName=obj_in.TableName)

        if table:
            obj_in_data = jsonable_encoder(obj_in)
            updated_table = db.update_table(**obj_in_data)

        return TableOut(TableName=table.TableName)

    def delete(self, dynamodb=None, *, table_name: str) -> None:
        if not dynamodb:
            dynamodb = get_db()

        db = dynamodb.get_resource()
        table = db.Table(table_name)
        table.delete()


table = CRUDTable(Table)
