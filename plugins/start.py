from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME as bn
from helpers.filters import other_filters2
from time import time
from datetime import datetime
from helpers.decorators import authorized_users_only
from config import BOT_USERNAME, ASSISTANT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/51da3e99d95a698d55ca5.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
I Cᴀɴ Pʟᴀʏ Mᴜsɪᴄ Iɴ Yᴏᴜʀ Gʀᴏᴜᴩ Vᴏɪᴄᴇ Cʜᴀᴛ. Dᴇᴠᴇʟᴏᴩᴇᴅ Bʏ 𝐒𝐮𝐦𝐢𝐭 𝐘𝐚𝐝𝐚𝐯.
Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴩ Aɴᴅ Pʟᴀʏ Mᴜsɪᴄ Fʀᴇᴇʟʏ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐋𝐢𝐬𝐭🧰", url="https://telegra.ph/text-10-24")
                  ],[
                    InlineKeyboardButton(
                       " 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="https://t.me/Social_Friends_Club"
                    ),
                    InlineKeyboardButton(
                        "𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url="https://t.me/Superiour_x_Server"
                    )
                ],[
                    InlineKeyboardButton(
                        "➕ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )
