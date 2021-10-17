import io

from pyrogram import Client
from pyrogram.types import Message

from Helpers import get_username, admin_only, ignore_channel, ignore_private, get_mention, get_mention_name
from InfinatoDB import DBMGMT
from cmdHandlers import smain


@smain("req", "#")
@ignore_channel
@ignore_private
async def _req(client: Client, message: Message):
    ac = DBMGMT.add("Requests",
                    {
                        "requested_by": get_mention_name(message.from_user),
                        "username": get_username(message.from_user),
                        "chat_id": message.chat.id,
                        "chat_title": message.chat.title,
                        "message_text": message.text
                    }
                    )
    await message.reply_text(
        f"{get_mention(message.from_user)} **Your Request Has Been Added to Database!**\n**Your Request_ID:** `{ac[1].id}`")


@smain("reqlist", "#")
@ignore_channel
@ignore_private
@admin_only
async def _reqlist(client: Client, message: Message):
    docs = DBMGMT.get("Requests")
    form = "**Request Id:** `{id}`\n**Request:** {val}\n\n"
    form2 = "Request Id: {id}\nRequest: {val}\n\n"
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
            resultFile.name = "RequestList.txt"
            await message.reply_document(document=resultFile, thumb="assets/cf2.jpg", caption="__Request List__")
    elif len(text) == 0:
        await message.reply_text("**Request List is Empty!**")
    else:
        await message.reply_text(text)


@smain("remreq", "#")
@ignore_channel
@ignore_private
@admin_only
async def _remreq(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("__Request Id Not Specified__")
    else:
        DBMGMT.rem("Requests", message.command[1])
        await message.reply_text(f"__Request Id__ {message.command[1]} __Removed__")
