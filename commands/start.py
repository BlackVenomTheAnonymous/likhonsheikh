from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    # Logic for handling the /start command
    # ...

# In the main.py file:
from commands.start import start

# Register the start command handler
dispatcher.add_handler(CommandHandler('start', start))
