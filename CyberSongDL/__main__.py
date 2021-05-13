# CyberHackers <https://t.me/Cyber0Hacker>
# @AmKuSaL

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from CyberSongDL.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from CyberSongDL import CHbot as app
from CyberSongDL import LOGGER

pm_start_text = """
Heya [{}](tg://user?id={}), I'm Song Downloader Bot 🎵 of CyberHackers Made By @AmKuSaL .

Do /help for know my commands

A bot by @Cyber0Hacker
"""

help_text = """
My commands👇

- /deezer <song name>: download songs via Deezer

A bot by @Cyber0Hacker
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Source", url="https://github.com/kusalCY/CyberSongDL"
                    ),
                    InlineKeyboardButton(
                        text="Developer", url="https://t.me/AmKuSaL"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def start(client, message):
    await message.reply(help_text)

app.start()
LOGGER.info("CyberSongDL is online.")
idle()
