from telegram.ext import Updater
from commands import start, bin, grab, gen, ac, cmds, sk, status, donet, copy

# Create an instance of the Updater and pass your bot token
updater = Updater('5951642700:AAFCSfs7l22xw3d21ZO3bOOA-2rI1S1lCc0', use_context=True)
dispatcher = updater.dispatcher

# Register the command handlers from the separate files
dispatcher.add_handler(start.handler)
dispatcher.add_handler(bin.handler)
dispatcher.add_handler(grab.handler)
dispatcher.add_handler(gen.handler)
dispatcher.add_handler(ac.handler)
dispatcher.add_handler(cmds.handler)
dispatcher.add_handler(sk.handler)
dispatcher.add_handler(status.handler)
dispatcher.add_handler(donet.handler)
dispatcher.add_handler(copy.handler)

# Run the bot
updater.start_polling()
updater.idle()
