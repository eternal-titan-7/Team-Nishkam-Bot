from pyrogram import Client
from pyrogram.types import Message

from Helpers import get_mention, admin_only, ignore_private, ignore_channel
from InfinatoDB import TagList
from cmdHandlers import smain


@smain("all", "@")
@ignore_channel
@ignore_private
@admin_only
async def _all(client: Client, message: Message):
    size = len(message.text[4:]) + 2
    txts = []
    c = 0
    async for pa in client.iter_chat_members(message.chat.id):
        if not (pa.user.is_bot or pa.user.is_deleted):
            if len(txts) == 0:
                txts.append(get_mention(pa.user))
            elif size + len(f"{txts[c]} {get_mention(pa.user)}") > 4096:
                c += 1
                txts.append(get_mention(pa.user))
            elif size + len(f"{txts[c]} {get_mention(pa.user)}") <= 4096:
                txts[c] += f" {get_mention(pa.user)}"
    for msg in txts:
        if message.reply_to_message:
            await message.reply_to_message.reply_text(f"{message.text[4:]}\n\n{msg}")
        else:
            await client.send_message(message.chat.id, f"{message.text[4:]}\n\n{msg}")


@smain("addtag", "@")
@ignore_channel
@ignore_private
@admin_only
async def _addtag(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("__List Name Not Specified__")
    elif not message.reply_to_message:
        await message.reply_text("__Reply to User You Want to Add to Tag List__")
    else:
        TagList.add(message.chat.id, message.command[1], get_mention(message.reply_to_message.from_user))
        await message.reply_text(
            f"{get_mention(message.reply_to_message.from_user)} __Added to Tag List__ `{message.command[1]}`")


@smain("remtag", "@")
@ignore_channel
@ignore_private
@admin_only
async def _remtag(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("__List Name Not Specified__")
    elif not message.reply_to_message:
        await message.reply_text("__Reply to User You Want to Remove From Tag List__")
    else:
        TagList.rem(message.chat.id, message.command[1], get_mention(message.reply_to_message.from_user))
        await message.reply_text(
            f"{get_mention(message.reply_to_message.from_user)} __Removed from Tag List__ `{message.command[1]}`")


@smain("taglist", "@")
@ignore_channel
@ignore_private
@admin_only
async def _taglist(client: Client, message: Message):
    taglist = TagList.sets(message.chat.id)
    if len(message.command) < 2:
        listOfTag = '`' + '`\n`'.join(taglist.keys()) + '`'
        await message.reply_text(f"__Showing Names of Lists because List Name Not Specified__\n\n{listOfTag}")
    elif message.command[1] not in taglist.keys():
        await message.reply_text(f"__List__ `{message.command[1]}` __is Empty__")
    elif len(taglist[message.command[1]]) == 0:
        await message.reply_text(f"__List__ `{message.command[1]}` __is Empty__")
    else:
        com = len('  '.join(message.command[:2]))
        size = len(message.text) + 2
        txts = []
        c = 0
        for ax in taglist[message.command[1]]:
            if len(txts) == 0:
                txts.append(ax)
            elif size + len(f"{txts[c]} {ax}") > 4096:
                c += 1
                txts.append(ax)
            elif size + len(f"{txts[c]} {ax}") <= 4096:
                txts[c] += f" {ax}"
        for msg in txts:
            if message.reply_to_message:
                await message.reply_to_message.reply_text(f"{message.text[com:]}\n\n{msg}")
            else:
                await client.send_message(message.chat.id, f"{message.text[com:]}\n\n{msg}")
