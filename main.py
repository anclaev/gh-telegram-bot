import os
import logging
from dotenv import load_dotenv
from bot import run

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

def main():
    TELEGRAM_BOT_API_TOKEN = os.getenv("TELEGRAM_BOT_API_TOKEN")

    if not TELEGRAM_BOT_API_TOKEN:
        logger.error("TELEGRAM_BOT_API_TOKEN не установлен.")
        quit(1)
    else:
        logger.log(logging.INFO, 'TELEGRAM_BOT_API_TOKEN загружен.')
        run(TELEGRAM_BOT_API_TOKEN)

load_dotenv()
main()