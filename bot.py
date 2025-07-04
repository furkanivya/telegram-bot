from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from telegram import Update
import os

TOKEN = os.getenv("TOKEN")  # .env içinden alıyorsan

async def show_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    print(f"📩 Chat ID: {chat.id} | Grup/Kişi Adı: {chat.title or chat.username}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, show_chat_id))
app.run_polling()
