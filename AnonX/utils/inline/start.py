           from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆ 𝐀𝐝𝐝 𝐌𝐞 𝐌𝐨𝐢 𝐋𝐮𝐯 ☆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🎭 𝐇𝐞𝐥𝐩 🎭",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="🕹️ 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬 🕹️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆ 𝐀𝐝𝐝 𝐌𝐞 𝐌𝐨𝐢 𝐋𝐮𝐯 ☆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="📍𝐌𝐀𝐍𝐓𝐀𝐈𝐍𝐄𝐑📍", url="t.me/taitangamerz",
            ),
            InlineKeyboardButton(
                text="🎭 𝐇𝐄𝐋𝐏 🎭", callback_data="settings_back_helper",
            )
        ],
        [
            InlineKeyboardButton(
                text="🍒 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🍒", url="dangerous_fighter_clan_0",
            ),
            InlineKeyboardButton(
                text="🏠 𝐆𝐑𝐎𝐔𝐏 🏠", url=f"https://t.me/timepassgroup01",
            )
        ],
        [
            InlineKeyboardButton(
                text="🌱 𝐎𝐖𝐍𝐄𝐑 🌱",
                url=f"https://t.me/taitangamerzz",
            )
        ],
     ]
    return buttons
