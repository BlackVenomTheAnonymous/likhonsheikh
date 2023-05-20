from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Create an instance of the Updater and pass your bot token
updater = Updater('YOUR_TELEGRAM_BOT_TOKEN', use_context=True)
dispatcher = updater.dispatcher
