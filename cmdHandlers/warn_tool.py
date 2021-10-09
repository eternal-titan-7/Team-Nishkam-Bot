from pyrogram import Client
from pyrogram.types import Message, ChatPermissions

from Helpers import ignore_private, ignore_channel, admin_only, get_mention
from InfinatoDB import DBMGMT


@ignore_channel
@ignore_private
@admin_only
async def _warn(client: Client, message: Message):
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
            "__Reply to User Message to Warn him/her\nOr Use Username or UserID__")
        return
    setting = DBMGMT.get("WARN", str(message.chat.id))
    warn = DBMGMT.get("WARN", f"{message.chat.id}/WARNINGS/{user.id}")
    reason = message.text[6:]
    if len(reason) == 0:
        reason = "No Reason"
    if setting:
        limit = setting["LIMIT"]
        action = setting["ACTION"]
    else:
        limit = 3
        action = "mute"
    if not warn:
        warn = {}
    cur_warns = len(warn.keys()) + 1
    warn[str(cur_warns)] = reason
    if cur_warns >= limit:
        try:
            if action.lower() == "mute":
                await client.restrict_chat_member(message.chat.id, user.id, ChatPermissions())
            elif action.lower() == "kick":
                await client.kick_chat_member(message.chat.id, user.id)
                await client.unban_chat_member(message.chat.id, user.id)
            elif action.lower() == "ban":
                await client.kick_chat_member(message.chat.id, user.id)
            await message.reply_text(
                "**‼ WARNING ‼**\n\n"
                f"**User:** {get_mention(user)}\n"
                f"**ID:** `{user.id}`\n"
                f"**Warns:** `{cur_warns}/{limit}`\n"
                f"**Reason:** `{reason}`\n"
                f"**Quick Action:** #{action.upper()}"
            )
        except:
            await message.reply_text(
                "**‼ WARNING ‼**\n\n"
                f"**User:** {get_mention(user)}\n"
                f"**ID:** `{user.id}`\n"
                f"**Warns:** `{cur_warns}/{limit}`\n"
                f"**Reason:** `{reason}`\n"
                f"**Quick Action:** #{action.upper()}\n\n"
                f"@admins Unable to perform Quick Action `{action.upper()}`"
            )
    else:
        await message.reply_text(
            "**‼ WARNING ‼**\n\n"
            f"**User:** {get_mention(user)}\n"
            f"**ID:** `{user.id}`\n"
            f"**Warns:** `{cur_warns}/{limit}`\n"
            f"**Reason:** `{reason}`\n"
        )
    DBMGMT.set("WARN", f"{message.chat.id}/WARNINGS/{user.id}", warn)


@ignore_channel
@ignore_private
@admin_only
async def _setwarn(client: Client, message: Message):
    try:
        limit = message.command[1]
        action = message.command[2]
    except:
        await message.reply_text(
            "Invalid Format of Command\n"
            "Format should be like /setwarn 10 mute\n"
            "Here, 10 is warn limit and mute is quick action\n"
            "Options of quick actions are mute, kick, ban")
        return
    if not ((limit.isdigit()) and (action.lower() in ["mute", "kick", "ban"])):
        await message.reply_text(
            "Invalid Format of Command\n"
            "Format should be like /setwarn 10 mute\n"
            "Here, 10 is warn limit and mute is quick action\n"
            "Options of quick actions are mute, kick, ban")
    else:
        limit = int(limit)
        action = action.lower()
        DBMGMT.set("WARN", str(message.chat.id), dict(LIMIT=limit, ACTION=action))
        await message.reply_text("**Warn Setting Has Been Set Successfully!**")


@ignore_channel
@ignore_private
@admin_only
async def _removewarn(client: Client, message: Message):
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
            "__Reply to User Message to Remove his/her Warn\nOr Use Username or UserID__")
        return
    DBMGMT.rem("WARN", f"{message.chat.id}/WARNINGS/{user.id}")
    await message.reply_text("**Warns Have Been Removed Successfully!")
