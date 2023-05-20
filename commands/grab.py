import re
import urllib.parse
import random

def grab(update, context):
    # Check if the user provided a link
    if len(context.args) == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please provide a valid Stripe buy link.")
        return

    # Extract information from the link using regex and urllib.parse
    link = context.args[0]
    pattern = r"pk_live_[\w-]+"
    match = re.search(pattern, link)
    if match:
        pk = match.group()
        cs = urllib.parse.parse_qs(urllib.parse.urlparse(link).query).get("cs", [""])[0]
        amount = urllib.parse.parse_qs(urllib.parse.urlparse(link).query).get("amount", [""])[0]
        email = urllib.parse.parse_qs(urllib.parse.urlparse(link).query).get("email", [""])[0]

        # Generate random emojis
        emojis = ["🔥", "💰", "✨", "🎉", "🌟"]
        random_emojis = [random.choice(emojis) for _ in range(5)]

        # Create a styled response with random emojis
        response = f"{random_emojis[0]} PK Live ✅: {pk}\n{random_emojis[1]} CS: {cs}\n{random_emojis[2]} Amount: {amount}\n{random_emojis[3]} Email: {email}"
        
        # Set the button link and text
        button_text = "𓆩𝗫𝗲𝗿𝗿𝗼𝘅𓆪「Zone ↯」"
        button_link = "https://t.me/xerrox_army"
        
        # Create the reply markup with the button
        
        # Send the response message with random emojis and the button
        context.bot.send_message(chat_id=update.effective_chat.id, text=response, reply_markup=reply_markup)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid Stripe buy link.")
