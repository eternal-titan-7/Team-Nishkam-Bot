from pyrogram import Client, filters
from pyrogram.types import Message

from Helpers import get_mention, get_display_name, get_username, admin_only
from InfinatoDB import DBMGMT


@Client.on_message(filters.command("setwelcome") & ~filters.channel)
@admin_only
async def setWel(client: Client, message: Message):
    if message.reply_to_message is None:
        await message.reply_text("__Reply to A Welcome Format__")
    else:
        form_data = dict(text=None, caption="", photo=None, video=None, sticker=None, document=None, audio=None,
                         voice=None, video_note=None, animation=None)
        if message.reply_to_message.text:
            form_data["text"] = message.reply_to_message.text
        if message.reply_to_message.caption:
            form_data["caption"] = message.reply_to_message.caption
        if message.reply_to_message.photo:
            form_data["photo"] = message.reply_to_message.photo.file_id
        elif message.reply_to_message.video:
            form_data["video"] = message.reply_to_message.video.file_id
        elif message.reply_to_message.document:
            form_data["document"] = message.reply_to_message.document.file_id
        elif message.reply_to_message.audio:
            form_data["audio"] = message.reply_to_message.audio.file_id
        elif message.reply_to_message.voice:
            form_data["voice"] = message.reply_to_message.voice.file_id
        elif message.reply_to_message.video_note:
            form_data["video_note"] = message.reply_to_message.video_note.file_id
        elif message.reply_to_message.animation:
            form_data["animation"] = message.reply_to_message.animation.file_id
        elif message.reply_to_message.sticker:
            form_data["sticker"] = message.reply_to_message.sticker.file_id
        DBMGMT.set("WELCOME", str(message.chat.id), form_data)
        await message.reply_text("__Welcome Note Saved__")


@Client.on_message(filters.command("setgoodbye") & ~filters.channel)
@admin_only
async def setBye(client: Client, message: Message):
    if message.reply_to_message is None:
        await message.reply_text("__Reply to A GoodBye Format__")
    else:
        form_data = dict(text=None, caption="", photo=None, video=None, sticker=None, document=None, audio=None,
                         voice=None, video_note=None, animation=None)
        if message.reply_to_message.text:
            form_data["text"] = message.reply_to_message.text
        if message.reply_to_message.caption:
            form_data["caption"] = message.reply_to_message.caption
        if message.reply_to_message.photo:
            form_data["photo"] = message.reply_to_message.photo.file_id
        elif message.reply_to_message.video:
            form_data["video"] = message.reply_to_message.video.file_id
        elif message.reply_to_message.document:
            form_data["document"] = message.reply_to_message.document.file_id
        elif message.reply_to_message.audio:
            form_data["audio"] = message.reply_to_message.audio.file_id
        elif message.reply_to_message.voice:
            form_data["voice"] = message.reply_to_message.voice.file_id
        elif message.reply_to_message.video_note:
            form_data["video_note"] = message.reply_to_message.video_note.file_id
        elif message.reply_to_message.animation:
            form_data["animation"] = message.reply_to_message.animation.file_id
        elif message.reply_to_message.sticker:
            form_data["sticker"] = message.reply_to_message.sticker.file_id
        DBMGMT.set("GOODBYE", str(message.chat.id), form_data)
        await message.reply_text("__GoodBye Note Saved__")


@Client.on_message(filters.command("clearwelcome") & ~filters.channel)
@admin_only
async def clearWel(client: Client, message: Message):
    DBMGMT.rem("WELCOME", str(message.chat.id))
    await message.reply_text("__Welcome Note Removed__")


@Client.on_message(filters.command("cleargoodbye") & ~filters.channel)
@admin_only
async def clearBye(client: Client, message: Message):
    DBMGMT.rem("GOODBYE", str(message.chat.id))
    await message.reply_text("__GoodBye Note Removed__")


@Client.on_message(filters.new_chat_members & ~filters.channel)
async def newMem(client: Client, message: Message):
    wel = DBMGMT.get("WELCOME", str(message.chat.id))
    if wel:
        count = len(await message.chat.get_members())
        for nm in message.new_chat_members:
            if wel["photo"]:
                await client.send_photo(message.chat.id, photo=wel["photo"], caption=wel["caption"].format(
                    mention=get_mention(nm),
                    title=message.chat.title,
                    members=count,
                    fullname=get_display_name(nm),
                    firstname=nm.first_name,
                    lastname=nm.last_name,
                    username=get_username(nm),
                    userid=nm.id,
                ))
            elif wel["video"]:
                await client.send_video(message.chat.id, video=wel["video"], caption=wel["caption"].format(
                    mention=get_mention(nm),
                    title=message.chat.title,
                    members=count,
                    fullname=get_display_name(nm),
                    firstname=nm.first_name,
                    lastname=nm.last_name,
                    username=get_username(nm),
                    userid=nm.id,
                ))
            elif wel["document"]:
                await client.send_document(message.chat.id, document=wel["document"], caption=wel["caption"].format(
                    mention=get_mention(nm),
                    title=message.chat.title,
                    members=count,
                    fullname=get_display_name(nm),
                    firstname=nm.first_name,
                    lastname=nm.last_name,
                    username=get_username(nm),
                    userid=nm.id,
                ))
            elif wel["audio"]:
                await client.send_audio(message.chat.id, audio=wel["audio"], caption=wel["caption"].format(
                    mention=get_mention(nm),
                    title=message.chat.title,
                    members=count,
                    fullname=get_display_name(nm),
                    firstname=nm.first_name,
                    lastname=nm.last_name,
                    username=get_username(nm),
                    userid=nm.id,
                ))
            elif wel["voice"]:
                await client.send_voice(message.chat.id, voice=wel["voice"], caption=wel["caption"].format(
                    mention=get_mention(nm),
                    title=message.chat.title,
                    members=count,
                    fullname=get_display_name(nm),
                    firstname=nm.first_name,
                    lastname=nm.last_name,
                    username=get_username(nm),
                    userid=nm.id,
                ))
            elif wel["video_note"]:
                await client.send_video_note(message.chat.id, video_note=wel["video_note"])
            elif wel["animation"]:
                await client.send_animation(message.chat.id, animation=wel["animation"])
            elif wel["sticker"]:
                await client.send_sticker(message.chat.id, sticker=wel["sticker"])
            elif wel["text"]:
                await client.send_message(message.chat.id, text=wel["text"].format(
                    mention=get_mention(nm),
                    title=message.chat.title,
                    members=count,
                    fullname=get_display_name(nm),
                    firstname=nm.first_name,
                    lastname=nm.last_name,
                    username=get_username(nm),
                    userid=nm.id,
                ))


@Client.on_message(filters.left_chat_member & ~filters.channel)
async def leftMem(client: Client, message: Message):
    wel = DBMGMT.get("GOODBYE", str(message.chat.id))
    if wel:
        count = len(await message.chat.get_members())
        nm = message.left_chat_member
        if wel["photo"]:
            await client.send_photo(message.chat.id, photo=wel["photo"], caption=wel["caption"].format(
                mention=get_mention(nm),
                title=message.chat.title,
                members=count,
                fullname=get_display_name(nm),
                firstname=nm.first_name,
                lastname=nm.last_name,
                username=get_username(nm),
                userid=nm.id,
            ))
        elif wel["video"]:
            await client.send_video(message.chat.id, video=wel["video"], caption=wel["caption"].format(
                mention=get_mention(nm),
                title=message.chat.title,
                members=count,
                fullname=get_display_name(nm),
                firstname=nm.first_name,
                lastname=nm.last_name,
                username=get_username(nm),
                userid=nm.id,
            ))
        elif wel["document"]:
            await client.send_document(message.chat.id, document=wel["document"], caption=wel["caption"].format(
                mention=get_mention(nm),
                title=message.chat.title,
                members=count,
                fullname=get_display_name(nm),
                firstname=nm.first_name,
                lastname=nm.last_name,
                username=get_username(nm),
                userid=nm.id,
            ))
        elif wel["audio"]:
            await client.send_audio(message.chat.id, audio=wel["audio"], caption=wel["caption"].format(
                mention=get_mention(nm),
                title=message.chat.title,
                members=count,
                fullname=get_display_name(nm),
                firstname=nm.first_name,
                lastname=nm.last_name,
                username=get_username(nm),
                userid=nm.id,
            ))
        elif wel["voice"]:
            await client.send_voice(message.chat.id, voice=wel["voice"], caption=wel["caption"].format(
                mention=get_mention(nm),
                title=message.chat.title,
                members=count,
                fullname=get_display_name(nm),
                firstname=nm.first_name,
                lastname=nm.last_name,
                username=get_username(nm),
                userid=nm.id,
            ))
        elif wel["video_note"]:
            await client.send_video_note(message.chat.id, video_note=wel["video_note"])
        elif wel["animation"]:
            await client.send_animation(message.chat.id, animation=wel["animation"])
        elif wel["sticker"]:
            await client.send_sticker(message.chat.id, sticker=wel["sticker"])
        elif wel["text"]:
            await client.send_message(message.chat.id, text=wel["text"].format(
                mention=get_mention(nm),
                title=message.chat.title,
                members=count,
                fullname=get_display_name(nm),
                firstname=nm.first_name,
                lastname=nm.last_name,
                username=get_username(nm),
                userid=nm.id,
            ))
