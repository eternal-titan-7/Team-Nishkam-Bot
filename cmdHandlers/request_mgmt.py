import io

from pyrogram import Client, filters
from pyrogram.types import Message

from DataBase import db


@Client.on_message(filters.command("req", "#") & ~filters.channel)
async def infReq(client: Client, message: Message):
    ac = db.collection("Requests").add(
        {
            "from_id": message.from_user.id,
            "from_name": ' '.join([message.from_user.first_name, message.from_user.last_name]),
            "from_username": f"@{message.from_user.username}",
            "chat_id": message.chat.id,
            "chat_title": message.chat.title,
            "message_text": message.text
        }
    )
    await message.reply_text(f"**Your Request Added to Database!**\n**Your Request_ID:** `{ac[1].id}`")


@Client.on_message(filters.command("reqlist", "#") & ~filters.channel)
async def infReqlst(client: Client, message: Message):
    db_ref = db.collection("Requests")
    db_stream = db_ref.stream()
    form = "**Request Id:** `{id}`\n**Request:** {val}\n\n"
    form2 = "Request Id: {id}\nRequest: {val}\n\n"
    text = ""
    text2 = ""
    for doc in db_stream:
        dict_form = []
        for k, v in doc.to_dict().items():
            dict_form.append(f"{k}: {v}")
        text += form.format(id=doc.id, val='\n'.join(dict_form))
        text2 += form2.format(id=doc.id, val=doc.to_dict())
    if len(text) > 4096:
        with io.BytesIO(text2.encode()) as resultFile:
            resultFile.name = "RequestList.txt"
            await message.reply_document(document=resultFile, thumb="assets/cf2.jpg", caption="__Request List__")
    elif len(text) == 0:
        await message.reply_text("**Request List is Empty!**")
    else:
        await message.reply_text(text)
