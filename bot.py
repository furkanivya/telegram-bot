from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from telegram import Update

# Gelen her mesajın chat ID'sini terminale yazdırır
async def show_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    print(f"📩 Chat ID: {chat.id} | Grup/Kişi Adı: {chat.title or chat.username}")

# BOT TOKENİNİ BURAYA YAZ (env kullanıyorsan TOKEN = os.getenv("TOKEN"))
TOKEN = "BURAYA_BOT_TOKENİNİ_YAZ"

# Uygulama başlat
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, show_chat_id))

print("🚀 Bot çalışıyor... Her gelen mesajın Chat ID'si terminale yazılacak.")
app.run_polling()
