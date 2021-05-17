from botocore.exceptions import ClientError
from fastapi import HTTPException, status
from typing import Optional, List, Any
from fastapi import APIRouter, Request
from loguru import logger


from app import crud, schemas
from app.utils.errors import handle_error


router = APIRouter()


@router.get("/", response_model=List[schemas.TableBase])
def get_tables(
    exclusive_start_table_name: Optional[str] = None,
    limit: int = 10,
):
    """
    ## Description
    List all tables in DynamoDB

    ## Parameters
    - **exclusive_start_table_name**: The table at which you want the list to start.
        - Use the value that was returned for **LastEvaluatedTableName** in a previous operation, so that you can obtain the next page of results.
    - **limit**: A maximum number of table names to return. If this parameter is not specified, the limit is 100.

    ## Return Type
    list
    """
    try:
        tables = crud.table.get_multi(
            exclusive_start_table_name=exclusive_start_table_name,
            limit=limit,
        )
        return tables
    except Exception as e:
        error = handle_error(e)
        logger.error(f"status_code={error.status_code}, detail={error.detail}")
        raise error


@router.get("/{table_name}", response_model=schemas.TableOut)
def get_table(table_name: str):
    """
    ## Description
    Returns information about the table, including the current status of the table, when it was created, the primary key schema, and any indexes on the table.

    ## Parameters
    - **table_name**: (string) -- [REQUIRED] The name of the table to describe.

    ## Return Type
    dict
    """
    try:
        response = crud.table.get(table_name=table_name)
        return response
    except Exception as e:
        raise e


@router.post("/", response_model=schemas.TableOut)
def create_table(table_in: schemas.TableCreate) -> Any:
    """
    Create a new Table in DynamoDB

    - **TableName**: str
    KeySchema: List[Key]
    AttributeDefinitions: List[AttributeDefinition]
    """
    try:
        new_table = crud.table.create(obj_in=table_in)
        return new_table
    except Exception as e:
        error = handle_error(e)
        logger.error(f"status_code={error.status_code}, detail={error.detail}")
        raise error


@router.put("/{table_name}", response_model=schemas.TableOut)
def update_table(table_name: str, attribute_definition: schemas.TableUpdate) -> schemas.TableOut:
    """
    AttributeDefinitions=[
        {
            'AttributeName': 'string',
            'AttributeType': 'S'|'N'|'B'
        },
    ],
    TableName='string',
    """
    try:
        attribute_definitions = [attribute_definition]
        obj_in = schemas.TableUpdate(TableName=table_name, AttributeDefinitions=attribute_definitions)
        print("obj_in", obj_in)

        response = crud.table.update(obj_in=obj_in)
        return response
    except ClientError as e:
        raise e


@router.delete("/")
def delete_table(table_name: str = None, dynamodb=None):
    try:
        crud.table.delete(dynamodb=dynamodb, table_name=table_name)
    except Exception as e:
        raise e
    else:
        return f"Successfully deleted {table_name} table!"


@router.post("/seed")
def seed_data(dynamodb=None):
    """TODO: Seed Data into local DynamoDb"""
    pass
    # if not dynamodb:
    #     dynamodb = boto3.resource("dynamodb", endpoint_url=settings.DYNAMODB_URL)

    #     data = []
    #     with open("./app/db/data/moviedata.json") as json_file:
    #         data = json.load(json_file, parse_float=Decimal)

    #     table = dynamodb.Table("Movies")
    #     for movie in data:
    #         year = int(movie["year"])
    #         title = movie["title"]
    #         table.put_item(Item=movie)
