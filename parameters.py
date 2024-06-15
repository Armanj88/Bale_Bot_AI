import logging
import os
from typing import Final

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Defines
TOKEN: Final = os.getenv("BOT_TOKEN")
LOG_FILE: Final = "logfile.log"

try:
    with open(os.getcwd() + "/" + LOG_FILE, 'w') as f:
        pass
except:
    pass

try:
    logging.basicConfig(
        filename=LOG_FILE,
        filemode="a",
        format="%(levelname)s:%(name)s:%(asctime)s:::%(message)s",
        level=logging.NOTSET,
    )
except:
    logging.basicConfig(
        level=logging.NOTSET,
    )
