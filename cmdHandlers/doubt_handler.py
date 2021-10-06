import io

from pyrogram import Client
from pyrogram.types import Message

from Helpers import get_username, admin_only, ignore_channel, ignore_private, get_mention, get_mention_name
from InfinatoDB import DBMGMT


@ignore_channel
@ignore_private
async def _doubt(client: Client, message: Message):
    ac = DBMGMT.add("Doubts",
                    {
                        "asked_by": get_mention_name(message.from_user),
                        "username": get_username(message.from_user),
                        "chat_id": message.chat.id,
                        "chat_title": message.chat.title,
                        "message_text": message.text
                    }
                    )
    await message.reply_text(
        f"{get_mention(message.from_user)} **Your Doubt Has Been Added to Database!**\n**Your Doubt_ID:** `{ac[1].id}`")


@ignore_channel
@ignore_private
@admin_only
async def _doubtlist(client: Client, message: Message):
    docs = DBMGMT.get("Doubts")
    form = "**Doubt Id:** `{id}`\n**Doubt:** {val}\n\n"
    form2 = "Doubt Id: {id}\nDoubt: {val}\n\n"
    text = ""
    text2 = ""
    for doc_id, doc in docs.items():
        dict_form = []
        for k, v in doc.items():
            dict_form.append(f"{k}: {v}")
        text += form.format(id=doc_id, val='\n'.join(dict_form))
        text2 += form2.format(id=doc_id, val=doc)
    if len(text) > 4096:
        with io.BytesIO(text2.encode()) as resultFile:
            resultFile.name = "DoubtList.txt"
            await message.reply_document(document=resultFile, thumb="assets/cf2.jpg", caption="__Doubt List__")
    elif len(text) == 0:
        await message.reply_text("**Doubt List is Empty!**")
    else:
        await message.reply_text(text)


@ignore_channel
@ignore_private
@admin_only
async def _remdoubt(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("__Doubt Id Not Specified__")
    else:
        DBMGMT.rem("Doubts", message.command[1])
        await message.reply_text(f"__Doubt Id__ {message.command[1]} __Removed__")
