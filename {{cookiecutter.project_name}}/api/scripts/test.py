import os


def test():
    """
    Run all tests. Equivalent to"
    `pytest -v`
    """
    os.system("pytest -v")


def coverage():
    """
    Run all tests. Equivalent to"
    `pytest --cov=alderaan-service app.tests/`
    """
    os.system("pytest --cov=alderaan-service tests/")
