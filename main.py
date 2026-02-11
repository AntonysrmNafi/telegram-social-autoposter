from telegram.ext import Application, CommandHandler
from config.settings import BOT_TOKEN
from bot.handlers import (
    help_handler,
    x_handler,
    linkedin_handler,
    facebook_handler,
    all_handler
)

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("help", help_handler))
    app.add_handler(CommandHandler("x", x_handler))
    app.add_handler(CommandHandler("linkedin", linkedin_handler))
    app.add_handler(CommandHandler("facebook", facebook_handler))
    app.add_handler(CommandHandler("all", all_handler))

    print("🤖 Bot started...")
    app.run_polling(allowed_updates=["message"])

if __name__ == "__main__":
    main()
