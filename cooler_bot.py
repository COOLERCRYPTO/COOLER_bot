import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Start Game", web_app=WebAppInfo(url="https://coolercrypto.github.io/COOLER_bot/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Hello! Welcome to CoolerGame. Press the button below to start the game.', reply_markup=reply_markup)

# Function to handle button presses
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == 'game_start':
        await query.edit_message_text(text="The game has started! Go ahead!")
        # Here you can add logic for starting the mini-application
        await start_game(query.message.chat_id, context)

# Function to start the mini-application
async def start_game(chat_id, context: ContextTypes.DEFAULT_TYPE):
    # Logic for starting the mini-application
    # For example, sending a message with instructions or a link to the mini-application
    await context.bot.send_message(chat_id=chat_id, text="Your computer is ready to farm COOLER!")

def main() -> None:
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set")
    
    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()


   # https://coolercrypto.github.io/COOLER_bot/


# 7476711537:AAHM1Kqv89wYNm-KiSsmYdhQy5_sK08MDm4