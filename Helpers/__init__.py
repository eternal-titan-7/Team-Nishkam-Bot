import io
import traceback
from typing import Callable

from pyrogram import Client
from pyrogram.raw.types import User
from pyrogram.types import Message

from Config import LOG_CHANNEL


def get_mention(user: User):
    if user.username:
        return f"@{user.username}"
    elif user.last_name and user.first_name:
        men = '{} {}'.format(user.first_name, user.last_name)
        return f"[{men}](tg://user?id={user.id})"
    elif user.first_name:
        return f"[{user.first_name}](tg://user?id={user.id})"
    elif user.last_name:
        return f"[{user.last_name}](tg://user?id={user.id})"
    else:
        return ''


def get_mention_name(user: User):
    if user.last_name and user.first_name:
        men = '{} {}'.format(user.first_name, user.last_name)
        return f"[{men}](tg://user?id={user.id})"
    elif user.first_name:
        return f"[{user.first_name}](tg://user?id={user.id})"
    elif user.last_name:
        return f"[{user.last_name}](tg://user?id={user.id})"
    else:
        return ''


def get_username(user: User):
    return f"@{user.username}" if user.username else None


def get_display_name(user: User):
    if user.first_name and user.last_name:
        return f"{user.first_name} {user.last_name}"
    elif user.first_name:
        return user.first_name
    elif user.last_name:
        return user.last_name
    else:
        return ''


def admin_only(func: Callable) -> Callable:
    async def decorators(client: Client, message: Message):
        members = await message.chat.get_members(filter="administrators")
        admins = []
        for us in members:
            admins.append(us.user.id)
        if message.from_user.id in admins:
            return await func(client, message)
        else:
            await message.reply_text("__This is Admin Only Command__")

    return decorators


def ignore_private(func: Callable) -> Callable:
    async def decorators(client: Client, message: Message):
        if message.chat.type != "private":
            return await func(client, message)

    return decorators


def ignore_channel(func: Callable) -> Callable:
    async def decorators(client: Client, message: Message):
        if message.chat.type != "channel":
            return await func(client, message)

    return decorators


def ignore_edited(func: Callable) -> Callable:
    async def decorators(client: Client, message: Message):
        if not message.edit_date:
            return await func(client, message)

    return decorators


def logs(func: Callable) -> Callable:
    async def decorators(client: Client, message: Message):
        try:
            await func(client, message)
        except Exception as err:
            trbk = traceback.format_exc()
            err_log = f"▩ **ERROR** ▩\n```{err}```\n▩ **TRACEBACK** ▩\n```{trbk}```"
            err_log2 = f"▩ ERROR ▩\n{err}\n▩ TRACEBACK ▩\n{trbk}"
            if len(err_log) > 4096:
                with io.BytesIO(err_log2.encode()) as resultFile:
                    resultFile.name = "err_log.txt"
                    await client.send_document(chat_id=LOG_CHANNEL, document=resultFile, thumb="assets/cf2.jpg",
                                               caption="__ERROR LOGS__")
            else:
                await client.send_message(LOG_CHANNEL, err_log)

    return decorators
