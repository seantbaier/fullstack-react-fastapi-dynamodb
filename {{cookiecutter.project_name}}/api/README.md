# FastAPI

## Installation

```shell
# Install Dependencies
pipenv install
```

## Run the application

```shell
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```

## Run Tests

```shell
pipenv run pytest
```

```shell
pipenv run pytest --cov --cov-fail-under=100
```
