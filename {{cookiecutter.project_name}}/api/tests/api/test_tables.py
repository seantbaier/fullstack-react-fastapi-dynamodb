from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient

from app.core.config import settings
from app import crud


def test_create_table(client: TestClient, test_table) -> None:
    response = client.post(f"{settings.API_V1_STR}/tables/", json=jsonable_encoder(test_table))

    assert response.status_code == 200
    content = response.json()

    assert content["TableName"] == test_table.TableName
    assert content["KeySchema"][0]["AttributeName"] == test_table.KeySchema[0].AttributeName
    assert content["KeySchema"][1]["AttributeName"] == test_table.KeySchema[1].AttributeName
    assert content["AttributeDefinitions"][0]["AttributeName"] == test_table.AttributeDefinitions[0].AttributeName
    assert content["AttributeDefinitions"][1]["AttributeName"] == test_table.AttributeDefinitions[1].AttributeName


def test_get_table(client: TestClient, test_table) -> None:
    new_table = crud.table.create(obj_in=test_table)
    response = client.get(f"{settings.API_V1_STR}/tables/{new_table.TableName}")

    assert response.status_code == 200
    content = response.json()

    assert content["TableName"] == new_table.TableName
    assert content["KeySchema"][0]["AttributeName"] == new_table.KeySchema[0].AttributeName
    assert content["KeySchema"][1]["AttributeName"] == new_table.KeySchema[1].AttributeName
    assert content["AttributeDefinitions"][0]["AttributeName"] == new_table.AttributeDefinitions[0].AttributeName
    assert content["AttributeDefinitions"][1]["AttributeName"] == new_table.AttributeDefinitions[1].AttributeName