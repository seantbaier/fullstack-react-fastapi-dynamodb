from typing import List

from fastapi.encoders import jsonable_encoder

from app.api.deps import get_db
from app.crud.base import CRUDBase
from app.models import Table
from app.schemas.table import TableCreate, TableUpdate


class CRUDTable(CRUDBase[Table, TableCreate, TableUpdate]):
    def get_multi(
        self, dynamodb=None, *, exclusive_start_table_name, limit: int = 15
    ) -> List[dict]:
        if not dynamodb:
            dynamodb = get_db()

        db = dynamodb.get_client()
        options = dict(Limit=limit)

        if exclusive_start_table_name:
            options["ExclusiveStartTableName"] = exclusive_start_table_name

        response = db.list_tables(**options)

        tables = []
        if "TableNames" in response:
            for name in response["TableNames"]:
                tables.append(dict(TableName=name))

        return tables

    def create(self, dynamodb=None, *, obj_in: TableCreate) -> Table:
        if not dynamodb:
            dynamodb = get_db()

        db = dynamodb.get_resource()
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)

        table = db.create_table(**dict(db_obj))

        return table

    def delete(self, dynamodb=None, *, table_name: str) -> None:
        if not dynamodb:
            dynamodb = get_db()

        db = dynamodb.get_resource()
        table = db.Table(table_name)
        table.delete()


table = CRUDTable(Table)
