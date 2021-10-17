from pyrogram import Client
from pyrogram.types import Message

from Helpers import admin_only, ignore_channel, ignore_private
from InfinatoDB import DBMGMT
from cmdHandlers import smain


@smain("dndon", "/")
@ignore_channel
@ignore_private
@admin_only
async def _dndon(client: Client, message: Message):
    DBMGMT.set("DND", str(message.chat.id), dict(dnd=True))
    await message.reply_text(
        "**DND Mode Set Successfully!**\n__Now Join and Left Messages will be deleted instantly\nAnd Welcome and GoodBye Messages will be deleted in A Minute__")


@smain("dndoff", "/")
@ignore_channel
@ignore_private
@admin_only
async def _dndoff(client: Client, message: Message):
    DBMGMT.rem("DND", str(message.chat.id))
    await message.reply_text("**DND Mode Deleted Successfully!**")
