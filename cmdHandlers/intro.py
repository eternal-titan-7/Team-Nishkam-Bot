from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from Helpers import ignore_channel


@ignore_channel
async def _start(client: Client, message: Message):
    await message.reply_cached_media(file_id="BAACAgQAAxkDAAOQYVxmmDJGE1TntAZjlrLD6TgRru0AAm4CAAIO9zVQS72lYy7fIpoeBA",
                                     caption="⚡️⚡️ Welcome To INFINATO ⚡️⚡️\n\nYou can send message to my master from here only, Just leave your text and I'll forward to my master.",
                                     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="MY MASTER",
                                                                                              url="https://t.me/INFINITY_I_i_I_i_I_i_I_i_I_i_I_i")]]))
