from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
SESSION_STRING = getenv("SESSION_STRING")
BOT_TOKEN = getenv("BOT_TOKEN")
LOG_CHANNEL = getenv("LOG_CHANNEL")
