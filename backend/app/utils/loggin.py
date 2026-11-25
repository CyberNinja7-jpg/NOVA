import logging
from pathlib import Path

from app.config import settings


LOG_FILE = settings.LOG_DIR / "nova.log"


def setup_logging():

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(
                LOG_FILE,
                encoding="utf-8"
            ),
            logging.StreamHandler()
        ]
    )


def get_logger(name: str):

    setup_logging()

    return logging.getLogger(name)
