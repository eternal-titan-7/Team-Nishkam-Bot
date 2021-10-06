from pyrogram import Client
from pyrogram.types import Message, ChatPermissions

from Helpers import get_mention, admin_only, ignore_channel, ignore_private, ignore_edited
from InfinatoDB import DBMGMT

md: dict[int, dict[int, list[int, int]]] = {}


@ignore_edited
@ignore_channel
@ignore_private
async def flood_handler(client: Client, message: Message):
    setting = DBMGMT.get("FLOOD", str(message.chat.id))
    if setting:
        members = await message.chat.get_members(filter="administrators")
        admins = []
        for us in members:
            admins.append(us.user.id)
        if message.from_user.id not in admins:
            if message.chat.id not in md.keys():
                md[message.chat.id] = {message.from_user.id: [message.date, 0]}
            else:
                if message.from_user.id not in md[message.chat.id].keys():
                    md[message.chat.id][message.from_user.id] = [message.date, 0]
                else:
                    limit: int = setting["LIMIT"]
                    action: str = setting["ACTION"]
                    a = md[message.chat.id][message.from_user.id][0]
                    b = message.date
                    if (b - a) < 3:
                        md[message.chat.id][message.from_user.id][1] += 1
                    else:
                        md[message.chat.id][message.from_user.id][1] = 0
                    if md[message.chat.id][message.from_user.id][1] >= limit:
                        try:
                            if action.lower() == "mute":
                                await client.restrict_chat_member(message.chat.id, message.from_user.id,
                                                                  ChatPermissions())
                            elif action.lower() == "kick":
                                await client.kick_chat_member(message.chat.id, message.from_user.id)
                                await client.unban_chat_member(message.chat.id, message.from_user.id)
                            elif action.lower() == "ban":
                                await client.kick_chat_member(message.chat.id, message.from_user.id)
                            await message.reply_text(
                                "__This User Has Reached Limit of Spamming__\n\n"
                                f"**User:** {get_mention(message.from_user)}\n"
                                f"**ID:** `{message.from_user.id}`\n"
                                f"**Limit:** `{limit}`\n"
                                f"**Quick Action:** #{action.upper()}"
                            )
                        except:
                            await message.reply_text(
                                "__This User Has Reached Limit of Spamming__\n\n"
                                f"**User:** {get_mention(message.from_user)}\n"
                                f"**ID:** `{message.from_user.id}`\n"
                                f"**Limit:** `{limit}`\n"
                                f"**Quick Action:** #{action.upper()}\n\n"
                                f"@admins Unable to perform Quick Action `{action.upper()}`"
                            )
                    md[message.chat.id][message.from_user.id][0] = message.date


@ignore_channel
@ignore_private
@admin_only
async def _setflood(client: Client, message: Message):
    try:
        limit = message.command[1]
        action = message.command[2]
    except:
        await message.reply_text(
            "Invalid Format of Command\n"
            "Format should be like /setflood 10 mute\n"
            "Here, 10 is flood limit and mute is quick action\n"
            "Options of quick actions are mute, kick, ban")
        return
    if not ((limit.isdigit()) and (action.lower() in ["mute", "kick", "ban"])):
        await message.reply_text(
            "Invalid Format of Command\n"
            "Format should be like /setflood 10 mute\n"
            "Here, 10 is flood limit and mute is quick action\n"
            "Options of quick actions are mute, kick, ban")
    else:
        limit = int(limit)
        action = action.lower()
        DBMGMT.set("FLOOD", str(message.chat.id), dict(LIMIT=limit, ACTION=action))
        await message.reply_text("**AntiFlood Has Been Set Successfully!**")


@ignore_channel
@ignore_private
@admin_only
async def _delflood(client: Client, message: Message):
    DBMGMT.rem("FLOOD", str(message.chat.id))
    await message.reply_text("**AntiFlood Has Been Deleted Successfully!")
