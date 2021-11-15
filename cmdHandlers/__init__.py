from typing import Callable

from pyrogram import Client
from pyrogram.types import Message

"""from cmdHandlers.admintools import _mute, _unmute, _ban, _unban, _kick
from cmdHandlers.dnd import _dndon, _dndoff
from cmdHandlers.doubt_handler import _doubt, _doubtlist, _remdoubt
from cmdHandlers.floodguard import _setflood, _delflood, flood_handler
from cmdHandlers.greets import _setwelcome, _setgoodbye, _clearwelcome, _cleargoodbye, newMem, leftMem
from cmdHandlers.intro import _start
from cmdHandlers.mention import _all, _addtag, _remtag, _taglist
from cmdHandlers.pyExec import _eval
from cmdHandlers.request_mgmt import _req, _reqlist, _remreq
from cmdHandlers.warn_tool import _warn, _setwarn, _removewarn"""
from Helpers import logs
from cmdHandlers._captor import sak


@Client.on_message()
@logs
async def mcheck(client: Client, message: Message):
    for hd in sak():
        if "flood" in hd["filters"]:
            await hd["func"](client, message)
        if ("newmem" in hd["filters"]) or message.new_chat_members:
            await hd["func"](client, message)
        if ("leftmem" in hd["filters"]) or message.left_chat_member:
            await hd["func"](client, message)
        if hd["cmd"]:
            message.command = message.text.strip(hd["trig"]).split()
            if message.command[0].lower() == hd["cmd"].lower():
                await hd["func"](client, message)


"""def stablize(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)

        return repl

    return layer"""


def smain(cmd: str = None, trig: str = None, filters=None):
    if filters is None:
        filters = []

    def ya(func: Callable):
        handler_data = {
            "func": func,
            "cmd": cmd,
            "trig": trig,
            "filters": filters
        }
        sak(handler_data)
        print(handler_data)

    return ya


"""@Client.on_message()
@logs
async def _(client: Client, message: Message):
    await flood_handler(client, message)
    if message.new_chat_members:
        await newMem(client, message)
    if message.left_chat_member:
        await leftMem(client, message)
    try:
        command1 = message.text.strip("/").split()
        command2 = message.text.strip("#").split()
        command3 = message.text.strip("@").split()
        message.command = command1
        if command1[0].lower() == "start":
            await _start(client, message)
        if command1[0].lower() == "eval":
            await _eval(client, message)
        if command1[0].lower() == "setwelcome":
            await _setwelcome(client, message)
        if command1[0].lower() == "setgoodbye":
            await _setgoodbye(client, message)
        if command1[0].lower() == "clearwelcome":
            await _clearwelcome(client, message)
        if command1[0].lower() == "cleargoodbye":
            await _cleargoodbye(client, message)
        if command1[0].lower() == "setflood":
            await _setflood(client, message)
        if command1[0].lower() == "delflood":
            await _delflood(client, message)
        if command1[0].lower() == "dndon":
            await _dndon(client, message)
        if command1[0].lower() == "dndoff":
            await _dndoff(client, message)
        if command1[0].lower() == "mute":
            await _mute(client, message)
        if command1[0].lower() == "unmute":
            await _unmute(client, message)
        if command1[0].lower() == "ban":
            await _ban(client, message)
        if command1[0].lower() == "unban":
            await _unban(client, message)
        if command1[0].lower() == "kick":
            await _kick(client, message)
        if command1[0].lower() == "warn":
            await _warn(client, message)
        if command1[0].lower() == "setwarn":
            await _setwarn(client, message)
        if command1[0].lower() == "removewarn":
            await _removewarn(client, message)
        message.command = command2
        if command2[0].lower() == "req":
            await _req(client, message)
        if command2[0].lower() == "reqlist":
            await _reqlist(client, message)
        if command2[0].lower() == "remreq":
            await _remreq(client, message)
        if command2[0].lower() == "doubt":
            await _doubt(client, message)
        if command2[0].lower() == "doubtlist":
            await _doubtlist(client, message)
        if command2[0].lower() == "remdoubt":
            await _remdoubt(client, message)
        message.command = command3
        if command3[0].lower() == "all":
            await _all(client, message)
        if command3[0].lower() == "addtag":
            await _addtag(client, message)
        if command3[0].lower() == "remtag":
            await _remtag(client, message)
        if command3[0].lower() == "taglist":
            await _taglist(client, message)
    except:
        pass"""
