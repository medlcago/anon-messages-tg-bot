import sys

from loguru import logger
from core.settings import BASE_DIR

logger.remove()
logger.add(f"{BASE_DIR}/file.log", rotation="1 MB", retention="10 days", compression="zip")
logger.add(sys.stderr, level="INFO")
