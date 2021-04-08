import pytest
from typing import Generator
from uuid import uuid4
from fastapi.testclient import TestClient

from app.core.config import settings
from app.db.client import dynamodb
from app.main import app
from app.schemas import TableCreate


@pytest.fixture(scope="session")
def db() -> Generator:
    yield dynamodb.client


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture()
def test_table():
    test_table_name = f"test_table_{uuid4()}"
    test_index_key = f"test_index_key_{uuid4()}"
    test_sort_key = f"test_sort_key_{uuid4()}"
    test_table = {
        "TableName": test_table_name,
        "KeySchema": [
            {"AttributeName": test_index_key, "KeyType": "HASH"},
            {"AttributeName": test_sort_key, "KeyType": "RANGE"},
        ],
        "AttributeDefinitions": [
            {"AttributeName": test_index_key, "AttributeType": "S"},
            {"AttributeName": test_sort_key, "AttributeType": "S"},
        ],
        "BillingMode": "PAY_PER_REQUEST",
        "Tags": [
            {"Key": f"test_tag_name_{uuid4()}", "Value": f"test_tag_value_{uuid4()}"}
        ],
    }

    table = TableCreate(**test_table)

    return table