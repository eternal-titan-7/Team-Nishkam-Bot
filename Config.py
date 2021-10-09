from InfinatoDB import DBMGMT

configuration = DBMGMT.get("TG_BOT", "CONFIG_")
API_ID = configuration.get("API_ID")
API_HASH = configuration.get("API_HASH")
SESSION_STRING = configuration.get("SESSION_STRING")
BOT_TOKEN = configuration.get("BOT_TOKEN")
LOG_CHANNEL = configuration.get("LOG_CHANNEL")
