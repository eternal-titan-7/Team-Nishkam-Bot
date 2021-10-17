from pyrogram import Client
from pyrogram.types import Message, ChatPermissions

from Helpers import admin_only, ignore_channel, ignore_private
from cmdHandlers import smain


@smain("mute", "/")
@ignore_channel
@ignore_private
@admin_only
async def _mute(client: Client, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    elif len(message.command) > 1:
        try:
            user = await client.get_users(message.command[1])
        except:
            await message.reply_text("__User Not Found__")
            return
    else:
        await message.reply_text("__Reply to User Message to Mute him/her\nOr Use Username or UserID__")
        return
    try:
        await client.restrict_chat_member(message.chat.id, user.id, ChatPermissions())
        await message.reply_text("**Successfully Muted!**")
    except:
        await message.reply_text("__Unable to Perform Requested Action__")


@smain("unmute", "/")
@ignore_channel
@ignore_private
@admin_only
async def _unmute(client: Client, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    elif len(message.command) > 1:
        try:
            user = await client.get_users(message.command[1])
        except:
            await message.reply_text("__User Not Found__")
            return
    else:
        await message.reply_text(
            "__Reply to User Message to Unmute him/her\nOr Use Username or UserID__")
        return
    try:
        await client.unban_chat_member(message.chat.id, user.id)
        await message.reply_text("**Successfully Unmuted!**")
    except:
        await message.reply_text("__Unable to Perform Requested Action__")


@smain("ban", "/")
@ignore_channel
@ignore_private
@admin_only
async def _ban(client: Client, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    elif len(message.command) > 1:
        try:
            user = await client.get_users(message.command[1])
        except:
            await message.reply_text("__User Not Found__")
            return
    else:
        await message.reply_text(
            "__Reply to User Message to Ban him/her\nOr Use Username or UserID__")
        return
    try:
        await client.kick_chat_member(message.chat.id, user.id)
        await message.reply_text("**Successfully Banned!**")
    except:
        await message.reply_text("__Unable to Perform Requested Action__")


@smain("unban", "/")
@ignore_channel
@ignore_private
@admin_only
async def _unban(client: Client, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    elif len(message.command) > 1:
        try:
            user = await client.get_users(message.command[1])
        except:
            await message.reply_text("__User Not Found__")
            return
    else:
        await message.reply_text(
            "__Reply to User Message to Unban him/her\nOr Use Username or UserID__")
        return
    try:
        await client.unban_chat_member(message.chat.id, user.id)
        await message.reply_text("**Successfully Unbanned!**")
    except:
        await message.reply_text("__Unable to Perform Requested Action__")


@smain("kick", "/")
@ignore_channel
@ignore_private
@admin_only
async def _kick(client: Client, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    elif len(message.command) > 1:
        try:
            user = await client.get_users(message.command[1])
        except:
            await message.reply_text("__User Not Found__")
            return
    else:
        await message.reply_text(
            "__Reply to User Message to Kick him/her\nOr Use Username or UserID__")
        return
    try:
        await client.kick_chat_member(message.chat.id, user.id)
        await client.unban_chat_member(message.chat.id, user.id)
        await message.reply_text("**Successfully Kicked!**")
    except:
        await message.reply_text("__Unable to Perform Requested Action__")
