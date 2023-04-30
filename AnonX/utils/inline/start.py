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
                text="☆ 𝐀𝐃𝐃 𝐌𝐄 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 ☆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="📍𝐌𝐀𝐈𝐍𝐓𝐀𝐈𝐍𝐄𝐑📍", url=f"https//t.me/taitangamerz
            ),
            InlineKeyboardButton(
                text="🎭 𝐇𝐄𝐋𝐏 🎭", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🍒 𝐆𝐑𝐎𝐔𝐏 🍒", url=f"https://t.me/timepassgroup01
            ),
            InlineKeyboardButton(
                text="🏠 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🏠", url=f"https://t.me/Dangerous_fighter_clan_1",
            )
        ],
        [
            InlineKeyboardButton(
                text="♛ 𝐎𝐖𝐍𝐄𝐑 ♛",
                url=f"https://t.me/taitangamerzz",
            )
        ],
     ]
    return buttons
