from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("start") & ~filters.channel)
async def infIntro(client: Client, message: Message):
    await message.reply_text("""
⚡️⚡️⚡️
**INFINATO's BOT**
**TEAM NISHKAM**
__धर्मो रक्षति रक्षितः__
⚡️⚡️⚡️
""")
