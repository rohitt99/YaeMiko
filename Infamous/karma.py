# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://graph.org/file/7c31b0b6bcaea61e5e236.jpg",
    "https://graph.org/file/daf0e8859c1922ea414e4.png",
    "https://graph.org/file/53cecd6ddac2438fa44fc.jpg",
    "https://graph.org/file/0f9d099b45074cb9a2ed3.png",
    "https://graph.org/file/8c68edda7a29ef01a92b8.jpg",
    "https://graph.org/file/01937fbb3f7c60104f60a.jpg",
    "https://graph.org/file/c3f9e65149f568b9891bb.jpg",
]

HEY_IMG = "https://graph.org/file/53cecd6ddac2438fa44fc.jpg"

ALIVE_ANIMATION = [
    "https://graph.org/file/acdef9bdb57502ce46ac3.mp4",
    "https://graph.org/file/ae86c56f2183f8fada1c0.mp4",
    "https://graph.org/file/acf9ed31939429215a40a.mp4",
    "https://graph.org/file/1ceadb2464668f17dac50.mp4",
    "https://graph.org/file/669efe1844cadc164c876.mp4",
    "https://graph.org/file/b13a4e69d74f37fbce5e5.mp4",
    "https://graph.org/file/51e40386b28d283940428.mp4",
    "https://graph.org/file/acdef9bdb57502ce46ac3.mp4",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ɪ ᴀᴍ 𝑰𝒎𝒑𝒆𝒓𝒊𝒍𝒎𝒆𝒏𝒕, ᴀ ɢᴇɴꜱʜɪɴ ɪᴍᴘᴀᴄᴛ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data="Miko_"),
        InlineKeyboardButton(text="AI", callback_data="ai_handler"),
        InlineKeyboardButton(text="SOURCE", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/IMPERILMENT_SUPPORT"),
        ib(text="SUPPORT", url="https://t.me/IMPERILMENT_SUPPORT"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *𝑰𝒎𝒑𝒆𝒓𝒊𝒍𝒎𝒆𝒏𝒕* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
