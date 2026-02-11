import os
from telegram import Update
from telegram.ext import ContextTypes
from bot.filters import allowed
from auth.x_oauth import get_x_auth_url, is_x_connected, remove_x_token
from auth.linkedin_oauth import get_linkedin_auth_url
from auth.facebook_oauth import get_facebook_auth_url

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not allowed(update):
        return

    await update.message.reply_text(
        "/x connect | /x <post> | /x disconnect\n"
        "/linkedin connect\n"
        "/facebook connect\n"
        "/all <post>"
    )

async def x_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not allowed(update):
        return

    if not context.args:
        await update.message.reply_text("Usage: /x connect | /x <post>")
        return

    cmd = context.args[0].lower()
    user_id = update.effective_user.id

    if cmd == "connect":
        if is_x_connected(user_id):
            await update.message.reply_text("✅ X already connected")
        else:
            await update.message.reply_text(get_x_auth_url(user_id))
        return

    if cmd == "disconnect":
        remove_x_token(user_id)
        await update.message.reply_text("❌ X disconnected")
        return

    if not is_x_connected(user_id):
        await update.message.reply_text("❌ Please connect your X account")
        return

    await update.message.reply_text("✅ Posted to X (posting logic here)")

async def linkedin_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not allowed(update):
        return
    await update.message.reply_text(get_linkedin_auth_url(update.effective_user.id))

async def facebook_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not allowed(update):
        return
    await update.message.reply_text(get_facebook_auth_url(update.effective_user.id))

async def all_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not allowed(update):
        return
    await update.message.reply_text("Posting to all connected platforms")
