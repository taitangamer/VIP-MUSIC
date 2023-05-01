from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆ 𝐀𝐃𝐃 𝐌𝐄 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 ☆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🎭 𝐇𝐄𝐋𝐏 🎭",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="🕹️ 𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒 🕹️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ 𝐀𝐃𝐃 𝐌𝐄 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𝐁𝐀𝐁𝐘 ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🔧 𝐇𝐄𝐋𝐏 & 𝐂𝐌𝐍𝐃 🔧", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 💥", url="https://t.me/dangerous_fighter_clan_0")

            InlineKeyboardButton(
                text="🥀 𝐆𝐑𝐎𝐔𝐏 💥", url="https://t.me/timepassgroup01")
        ],
        [
            InlineKeyboardButton(
                text="♕︎ 𝐎𝐖𝐍𝐄𝐑 ♕", url="https://t.me/taitangamerzz")
            )
        ],
     ]
    return buttons
