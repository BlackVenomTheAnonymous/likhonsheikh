# In your main script or wherever you initialize the Telegram bot:
from commands.copy import copy, status
from telegram.ext import CommandHandler

# Register the copy command handler
dispatcher.add_handler(CommandHandler("copy", copy))

# Register the status command handler
dispatcher.add_handler(CommandHandler("status", status))
