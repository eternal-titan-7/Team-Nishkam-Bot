from pyrogram import Client

import ENV_VARS

infUser = None


async def start():
    global infUser
    infUser = Client(session_name=ENV_VARS.SESSION_STRING, api_id=ENV_VARS.API_ID, api_hash=ENV_VARS.API_HASH,
                     bot_token=ENV_VARS.BOT_TOKEN)
    await infUser.start()
