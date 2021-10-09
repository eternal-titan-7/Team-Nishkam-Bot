import asyncio
from pyrogram import Client
import tgcrypto
import Config
import inf


async def main():
    await inf.start()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    infBot = Client(session_name=":memory:", api_id=Config.API_ID, api_hash=Config.API_HASH,
                    bot_token=Config.BOT_TOKEN, plugins=dict(root="cmdHandlers"))
    infBot.run()
