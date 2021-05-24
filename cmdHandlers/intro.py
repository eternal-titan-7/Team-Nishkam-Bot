from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("start") & ~filters.channel)
async def infIntro(client: Client, message: Message):
    await message.reply_video(video="https://telegra.ph/file/514a1c7cb71a7e910f081.mp4", thumb="assets/cf2.jpg", caption="""
⚡️⚡️⚡️
**TEAM NISHKAM**
__धर्मो रक्षति रक्षितः__
⚡️⚡️⚡️

 - `Made By INFINATO :)`
""")
