import logging
import os
from typing import Final

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Defines
TOKEN: Final = os.getenv("BOT_TOKEN")
LOG_FILE: Final = ".log"

with open(LOG_FILE, 'w') as f:
    pass

logging.basicConfig(
    filename=LOG_FILE,
    filemode="a",
    format="%(levelname)s:%(name)s:%(asctime)s:::%(message)s",
    level=logging.NOTSET,
)
