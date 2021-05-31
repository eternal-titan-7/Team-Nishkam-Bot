from typing import Callable

from pyrogram import Client
from pyrogram.raw.types import User
from pyrogram.types import Message


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
            await func(client, message)
        else:
            await message.reply_text("__This is Admin Only Command__")

    return decorators
