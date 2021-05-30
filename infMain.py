import asyncio
from pyrogram import Client
import tgcrypto
import ENV_VARS
import inf


async def main():
    await inf.start()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    infBot = Client(session_name=":memory:", api_id=ENV_VARS.API_ID, api_hash=ENV_VARS.API_HASH,
                    bot_token=ENV_VARS.BOT_TOKEN, plugins=dict(root="cmdHandlers"))
    infBot.run()
