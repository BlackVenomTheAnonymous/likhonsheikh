from commands.copy import copy, status
from telegram.ext import CommandHandler
def register_handlers(dispatcher):
    # Register the copy command handler
    dispatcher.add_handler(CommandHandler("copy", copy))

    # Register the status command handler
    dispatcher.add_handler(CommandHandler("status", status))
    from handlers import register_handlers
    
