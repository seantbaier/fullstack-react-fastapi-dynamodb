virtual:
	python3 -m venv env

source:
	source env/bin/activate

clean:
	find . -type d -name '__pycache__' -exec rm -r -v {} +
	find . -type d -name '\.pytest_cache' -exec rm -r -v {} +
	find . -type d -name 'function' -exec rm -r -v {} +
	find . -type f -name '*.pyc'  -delete
	find . -type f -name 'function.zip'  -delete

bundle: clean
	bin/bundle.sh

install:
	pip install -r requirements.txt

lint:
	black .
	pylint *.py

db:
	docker-compose up

docker-build:
	docker build -t fastapi .

docker-run:
	docker run -d --name fastapi -p 80:80 fastapi

docker-test:
	docker-compose -f docker-compose.test.yml up --exit-code-from fastapi

test:
	RUNTIME_ENVIRONMENT=test pytest -v

coverage:
	RUNTIME_ENVIRONMENT=test pytest --cov=src tests/

run:
	uvicorn app.main:app --reload --port 8080