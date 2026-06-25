import logging
import os
from datetime import datetime


LOG_FILE_NAME = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOGS_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE_NAME)
os.makedirs(os.path.dirname(LOGS_PATH), exist_ok=True)

logging.basicConfig(
filename=LOGS_PATH,
format="%(asctime)s - %(lineno)d - %(levelname)s - %(message)s",
level=logging.INFO,
)
