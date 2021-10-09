from pyrogram import Client

import Config

infUser = None


async def start():
    global infUser
    infUser = Client(session_name=Config.SESSION_STRING, api_id=Config.API_ID, api_hash=Config.API_HASH,
                     bot_token=Config.BOT_TOKEN)
    await infUser.start()
