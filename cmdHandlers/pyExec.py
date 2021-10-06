import io
import sys
import traceback

from pyrogram import Client, filters
from pyrogram.types import Message

from Helpers import ignore_channel


@ignore_channel
async def _eval(client: Client, message: Message):
    msg = await message.reply_text("**Proccessing...**")
    code = message.text[6:]
    if len(code) == 0:
        await msg.edit_text("__Please Provide the Python Code!__")
        return
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    stdout = None
    stderr = None
    trbk = None
    code_out = sys.stdout = io.StringIO()
    code_err = sys.stderr = io.StringIO()
    try:
        await aexec(code, client, message)
    except:
        trbk = traceback.format_exc()
    stdout = code_out.getvalue()
    stderr = code_err.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    results = dict(code=f"▩ **CODE :**\n```{code}```\n", out="", err="", trbk="")
    results2 = dict(code=f"▩ CODE :\n{code}\n", out="", err="", trbk="")
    if stdout:
        results["out"] = f"▩ **OUTPUT :**\n```{stdout}```\n"
        results2["out"] = f"▩ OUTPUT :\n{stdout}\n"
    if stderr:
        results["err"] = f"▩ **ERROR :**\n```{stderr}```\n"
        results2["err"] = f"▩ ERROR :\n{stderr}\n"
    if trbk:
        results["trbk"] = f"▩ **TRACEBACK :**\n```{trbk}```\n"
        results2["trbk"] = f"▩ TRACEBACK :\n{trbk}\n"
    result = '\n'.join([results["code"], results["out"], results["err"], results["trbk"]])
    if len(result) > 4096:
        result = '\n'.join([results2["code"], results2["out"], results2["err"], results2["trbk"]])
        with io.BytesIO(result.encode()) as resultFile:
            resultFile.name = "result.txt"
            await message.reply_document(document=resultFile, thumb="assets/cf2.jpg", caption="__Code Run Results__")
            await msg.delete()
    else:
        await msg.edit_text(result)


async def aexec(code, client: Client, message: Message):
    c = client
    e = message
    exec(
        f"async def __aexec(c, e): "
        + "".join(f"\n {i}" for i in code.split("\n")),
    )
    return await locals()["__aexec"](c, e)
