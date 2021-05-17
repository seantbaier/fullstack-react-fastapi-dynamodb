import logging

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed
from pynamodb.connection import Connection

from app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.DEBUG),
)
def init() -> None:
    try:
        conn = Connection(
            host=settings.DYNAMODB_LOCAL_URL, region=settings.AWS_DEFAULT_REGION
        )

        # Check to see if connection is established.
        conn.list_tables()
    except ConnectionRefusedError as e:
        logger.error(e)
        raise Exception("Database connection failed.")
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
