import stripe
from telegram import Update
from telegram.ext import CallbackContext

def sk(update: Update, context: CallbackContext):
    # Get the Stripe SK key from the user's input
    sk_key = update.message.text.split('/sk ')[1]

    # Initialize Stripe with the SK key
    stripe.api_key = sk_key

    try:
        # Retrieve the account details using the SK key
        account = stripe.Account.retrieve()

        # Check if the account is active
        if account['charges_enabled']:
            response = "The Stripe SK key is alive and active! ✅"
        else:
            response = "The Stripe SK key is alive but not active. ❌"

    except stripe.error.AuthenticationError:
        response = "The Stripe SK key is invalid or unauthorized. ❌"

    # Send the response message to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Register the sk command handler
dispatcher.add_handler(CommandHandler('sk', sk))
