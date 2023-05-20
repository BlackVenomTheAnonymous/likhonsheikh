import requests
import random
import time

def bin(update, context):
    # Get the user input from the command
    user_input = context.args[0]

    # Send loading message
    loading_message = context.bot.send_message(chat_id=update.effective_chat.id, text="🔍 Loading BIN data... ⏳")

    # Simulate a delay for 3 seconds
    time.sleep(3)

    # Remove the loading message
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=loading_message.message_id)

    # Make a GET request to the API with the user input
    response = requests.get(f"https://lookup.binlist.net/{user_input}")

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extract the relevant information from the response
        scheme = data.get('scheme')
        brand = data.get('brand')
        card_type = data.get('type')
        country = data.get('country', {}).get('name')
        bank_name = data.get('bank', {}).get('name')
        bank_url = data.get('bank', {}).get('url')
        bank_phone = data.get('bank', {}).get('phone')
        bank_city = data.get('bank', {}).get('city')

        # Generate random emojis
        random_emojis = [random.choice(['🌍', '🌎', '🌏']), random.choice(['🏢', '🏦', '🏪']), random.choice(['📞', '☎️', '📱']), random.choice(['🏙️', '🌆', '🏢']), random.choice(['🔢', '🆔', '💳'])]

        # Create the response message with the extracted information and random emojis
        message = "✅ <b>BIN Data:</b>\n\n"
        message += f"<b>BIN:</b> {user_input} {random_emojis[4]}\n\n"
        message += f"<b>Scheme:</b> {scheme}\n"
        message += f"<b>Brand:</b> {brand}\n"
        message += f"<b>Type:</b> {card_type}\n\n"
        message += f"<b>Country:</b> {country} {random_emojis[0]}\n\n"
        message += f"<b>Bank:</b> {bank_name}\n"
        message += f"<b>URL:</b> {bank_url} {random_emojis[1]}\n"
        message += f"<b>Phone:</b> {bank_phone} {random_emojis[2]}\n"
        message += f"<b>City:</b> {bank_city} {random_emojis[3]}\n"

        # Add the inline button to the message
        button_text = f"{random_emojis[0]} {random_emojis[1]} {random_emojis[2]} {random_emojis[3]} {random_emojis[4]} 𓆩𝗫𝗲𝗿𝗿𝗼𝘅𓆪「Zone ↯」"
        button_link = "https://t.me/xerrox_army"
        message += f"\n\n{button_text} - {button_link}"

        # Send
