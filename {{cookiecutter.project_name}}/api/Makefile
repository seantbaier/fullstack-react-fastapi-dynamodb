virtual:
	virtualenv -p python3.8 env

source:
	source env/bin/activate

clean:
	find . -type d -name '__pycache__' -exec rm -r -v {} +
	find . -type d -name '\.pytest_cache' -exec rm -r -v {} +
	find . -type d -name 'function' -exec rm -r -v {} +
	find . -type f -name '*.pyc'  -delete
	find . -type f -name 'function.zip'  -delete
	find . -type f -name '/tmp/list_file.csv'  -delete

install:
	pip install -r requirements.txt

lint:
	black .
	pylint *.py

test:
	ENVIRONMENT=TEST pytest -v

coverage: 
	ENVIRONMENT=TEST pytest --cov=src tests/

run:
	uvicorn app.main:app --reload
