from .core.get_config import get_var
from .core.handlers import add_handlers
from .mesh_bot import MeshRenameBot
from . maneuvers.ExecutorManager import ExecutorManager
from pyrogram import Client, filters
from config import Commands
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

# TODO Add a alert for an extra space recorded

if __name__ == "__main__":

    rbot = MeshRenameBot("MeshRenameBot", get_var("API_ID"), get_var("API_HASH"), 
                         bot_token=get_var("BOT_TOKEN"), workers=200)
    excm = ExecutorManager()
    add_handlers(rbot)
    rbot.run()
@Client.on_message(filters.command(""))
async def invalid_cmd(bot, cmd):
    invldcmd = cmd.text
    invldcmd = invldcmd.replace("/","")
    if invldcmd not in Commands :
        await cmd.reply("Sorry you are not authorised by [**MK**](https://t.me/ManuKriz)",parse_mode="Markdown",disable_web_page_preview=True)
    else :
        return
