# Cleaned Redeem.py (Premium Removed Completely)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import ADMINS

# Redeem / premium system is disabled in your bot.
# This file now only returns a simple message.

@Client.on_message(filters.command("add_redeem") & filters.user(ADMINS))
async def add_redeem_code(client, message):
    await message.reply_text(
        "<b>⚠️ Redeem system is disabled.\nPremium features are removed from this bot.</b>"
    )

@Client.on_message(filters.command("redeem"))
async def redeem_code(client, message):
    await message.reply_text(
        "<b>❌ Redeem feature is no longer available.\nThis bot has no premium system.</b>"
    )
