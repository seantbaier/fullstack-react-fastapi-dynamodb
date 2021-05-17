FROM python:3.8

RUN pip install --no-cache-dir "uvicorn[standard]" gunicorn

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
  cd /usr/local/bin && \
  ln -sf /opt/poetry/bin/poetry && \
  poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /

RUN poetry install --no-root

# See dockerignore for which files this is copying
COPY . .

ENV PYTHONPATH=/app

EXPOSE 80
