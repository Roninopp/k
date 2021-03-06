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


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**Hey, I'm {bn} ๐
I Cแดษด Pสแดส Mแดsษชแด Iษด Yแดแดส Gสแดแดแดฉ Vแดษชแดแด Cสแดแด. Dแดแด แดสแดแดฉแดแด Bส ๐๐ฎ๐ฆ๐ข๐ญ ๐๐๐๐๐ฏ.
Aแดแด Mแด Tแด Yแดแดส Gสแดแดแดฉ Aษดแด Pสแดส Mแดsษชแด Fสแดแดสส!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐๐จ๐ฆ๐ฆ๐๐ง๐ ๐๐ข๐ฌ๐ญ๐งฐ", url="https://telegra.ph/text-10-24")
                  ],[
                    InlineKeyboardButton(
                       " ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ", url="https://t.me/Social_Friends_Club"
                    ),
                    InlineKeyboardButton(
                        "๐๐ฉ๐๐๐ญ๐๐ฌ", url="https://t.me/Superiour_x_Server"
                    )
                ],[
                    InlineKeyboardButton(
                        "โ ๐๐๐ ๐๐ ๐๐จ ๐๐จ๐ฎ๐ซ ๐๐ซ๐จ๐ฎ๐ฉโ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )
