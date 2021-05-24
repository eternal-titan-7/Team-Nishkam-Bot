from pyrogram import Client

import vars

infBot = Client(session_name=":memory:", api_id=vars.API_ID, api_hash=vars.API_HASH, bot_token=vars.BOT_TOKEN, plugins=dict(root="cmdHandlers"))
infBot.run()
