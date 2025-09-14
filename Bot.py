import os
from gtts import gTTS
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# === Apna Telegram Bot Token yaha paste karein ===
BOT_TOKEN = "8231103596:AAEPeYdyP7PDyY7n3uQ36dyEjAqdlLbz2ek"

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Namaste! Main Text-to-Speech Bot hoon.\n\n"
        "Aap mujhe koi bhi text bhejein aur main usko voice me convert karke dunga.\n\n"
        "Commands:\n"
        "/help - Madad ke liye"
    )

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 Madad:\n\n"
        "1️⃣ Koi bhi text message bhejein.\n"
        "2️⃣ Main uska voice file banakar wapas bhej dunga.\n"
        "3️⃣ Hindi aur English dono text support karta hai."
    )

# Text ko voice me convert karke bhejna
async def text_to_speech(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if not text or text.startswith("/"):
        return  # Ignore commands

    try:
        # gTTS ka use karke text ko voice me convert karein
        tts = gTTS(text=text, lang="hi")  # "hi" Hindi ke liye, "en" English ke liye
        file_path = "voice.mp3"
        tts.save(file_path)

        # Audio file bhejna
        with open(file_path, "rb") as audio:
            await update.message.reply_voice(voice=audio, caption="🔊 Aapka voice message ready hai!")

        # Temporary file delete karein
        os.remove(file_path)

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")

# Main function
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_to_speech))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
