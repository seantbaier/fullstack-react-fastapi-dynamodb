from app import crud
from app.schemas import TableCreate


def test_create_table(test_table: TableCreate) -> None:
    new_table = crud.table.create(obj_in=test_table)

    assert new_table.TableName == test_table.TableName
    assert new_table.KeySchema[0].AttributeName == test_table.KeySchema[0].AttributeName
    assert new_table.KeySchema[1].AttributeName == test_table.KeySchema[1].AttributeName
    assert new_table.AttributeDefinitions[0].AttributeName == test_table.AttributeDefinitions[0].AttributeName
    assert new_table.AttributeDefinitions[1].AttributeName == test_table.AttributeDefinitions[1].AttributeName


def test_get_table(test_table: TableCreate) -> None:
    new_table = crud.table.create(obj_in=test_table)
    table = crud.table.get(table_name=new_table.TableName)

    assert table.TableName == test_table.TableName
    assert table.KeySchema[0].AttributeName == test_table.KeySchema[0].AttributeName
    assert table.KeySchema[1].AttributeName == test_table.KeySchema[1].AttributeName
    assert table.AttributeDefinitions[0].AttributeName == test_table.AttributeDefinitions[0].AttributeName
    assert table.AttributeDefinitions[1].AttributeName == test_table.AttributeDefinitions[1].AttributeName