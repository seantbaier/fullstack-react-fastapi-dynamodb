import os
from pathlib import Path


def start():
    """
    Run the app locally without Docker
    """
    os.system("docker-compose up -d localstack")

    path = Path.cwd().joinpath("bin", "start-reload.sh")
    os.system(f"PORT=8000 sh {path}")


def docker():
    """
    Run app with docker
    """
    os.system("docker-compose up --build")
