import os
from config import Config
from .fonts import Fonts
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command('start'))
async def start(c, m):
    owner = await c.get_users(int(Config.OWNER_ID))
    owner_username = owner.username if owner.username else 'Ns_bot_updates'

    # start text
    text = f"""Hey! {m.from_user.mention(style='md')},
💡 ** I am Stylish Font Bot**
`I can help you to get stylish fonts. Just send me some text and see magic.`
**👲 Maintained By:** {owner.mention(style='md')}
"""

    # Buttons
    buttons = [
        [InlineKeyboardButton('My Father 👨‍✈️', url=f"https://t.me/{owner_username}]]
        [InlineKeyboardButton('🤖 Bot Updates', url=f"https://t.me/Bx_Botz)]]
        [InlineKeyboardButton('Support Group', url=f"https://t.me/BxSupport)]]

    await m.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
