import asyncio

from pyrogram import Client

print("INFINATO SESSION STRING GENERATOR\n")


async def main():
    api_id = int(input("ENTER API ID:"))
    api_hash = input("ENTER API HASH:")
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as infinato:
        session = await infinato.export_session_string()
        if (await infinato.get_me()).is_bot:
            bot = input("Enter the username: ")
            await infinato.send_message(bot,
                                        f"**FOLLOWING IS YOUR INFINATO-BOT STRING SESSION**\n`{session}`\n**Generated Using INFINATO STRING SESSION GENERATOR**\n\n**Don't Share To Anyone :)**")
            print("\nPlease Check Your Telegram's DM for String Session.")
        else:
            await infinato.send_message("me",
                                        f"**FOLLOWING IS YOUR INFINATO-BOT STRING SESSION**\n`{session}`\n**Generated Using INFINATO STRING SESSION GENERATOR**\n\n**Don't Share To Anyone :)**")
            print("\nPlease Check Your Telegram's Saved Messages for String Session.")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
