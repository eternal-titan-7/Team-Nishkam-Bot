import io

from pyrogram import Client, filters
from pyrogram.types import Message

from Helpers import get_display_name, get_username, admin_only
from InfinatoDB import DBMGMT


@Client.on_message(filters.command("req", "#") & ~filters.channel)
async def infReq(client: Client, message: Message):
    ac = DBMGMT.add("Requests",
                    {
                        "from_id": message.from_user.id,
                        "from_name": get_display_name(message.from_user),
                        "from_username": get_username(message.from_user),
                        "chat_id": message.chat.id,
                        "chat_title": message.chat.title,
                        "message_text": message.text
                    }
                    )
    await message.reply_text(f"**Your Request Added to Database!**\n**Your Request_ID:** `{ac[1].id}`")


@Client.on_message(filters.command("reqlist", "#") & ~filters.channel)
@admin_only
async def infReqlst(client: Client, message: Message):
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


@Client.on_message(filters.command("remreq", "#") & ~filters.channel)
@admin_only
async def remReq(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("__Request Id Not Specified__")
    else:
        DBMGMT.rem("Requests", message.command[1])
        await message.reply_text(f"__Request Id__ {message.command[1]} __Removed__")
