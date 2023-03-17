import asyncio
from pyrogram import Client, filters
from config import BANNED_USERS
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)

from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

AM_COMMAND = get_command("AM_COMMAND")


@app.on_message(
    command(AM_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
async def khalid(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/138c2ffc68f8fc77bf97a.jpg",
        caption=f"""✧ اهـلا بيك في اوامر بوت سيـا\n\n -› **جميع اوامر البوت موجودة بالقائمة ، اضغط الازرار الي تحت واستكشف**\n\n• Developer -› [⎖᳒𝐁𝐎𝐨𝐒 𝐇𝐚𝐌𝐚𝐒𝐚](t.me/Y_F_G5)\n• Channel -› [𝙎𝙨𝙞𝘼𝙖 𝙈𝘂𝙎𝗶𝘾](t.me/UI_IUSIA)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "شرح التشغيل بمنصات الاغاني", callback_data=f"ko"),
                ],[
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data=f"ddd"),

                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data=f"tt"),

                ],[
                    InlineKeyboardButton(
                        "ربط القنوات", callback_data=f"cha"),

                    InlineKeyboardButton(
                        "اوامر البحث", callback_data=f"don"),
                ],[

                    InlineKeyboardButton(
                        "حفظ التشغيل", callback_data=f"save"),

                    InlineKeyboardButton(
                        "اوامر خدمية", callback_data=f"kdm"),
                ],[

                    InlineKeyboardButton(
                        "تحديثات سيـا 🥢", url=f"https://t.me/UI_IUSIA"),

                ],
            ]
        ),
    )
