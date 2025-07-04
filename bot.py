import os
from telegram.ext import Updater, CommandHandler

# Token .env'den veya Render ortam değişkenlerinden alınır
TOKEN = os.environ.get("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("Merhaba Hilal! Botun başarıyla çalışıyor ✨")

def help_command(update, context):
    update.message.reply_text("Yardım için buradayım. /start yazarak başlayabilirsin!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Komutlar
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
