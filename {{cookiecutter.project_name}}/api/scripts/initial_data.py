from loguru import logger

from app.db.init_db import init_db


def init() -> None:
    init_db()


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
