import random
import time

def gen(update, context):
    # Get the parameters from the user's message
    params = context.args

    if len(params) < 2:
        # Insufficient parameters, send an error message
        update.message.reply_text("Invalid command! Usage: /gen <BIN> <Amount>")
        return

    bin_number = params[0]
    amount = params[1]

    # Generate credit card information
    card_number = generate_card_number(bin_number)
    cvv = generate_cvv()
    expiration_date = generate_expiration_date()

    # Create the card information text with random emojis
    card_info = f"🔒 Card Number: {card_number}\n🔑 CVV: {cvv}\n📆 Expiration Date: {expiration_date}"

    # Save the card information to a temporary file with random emojis
    temp_filename = 'temp_card_info.txt'
    save_to_file(temp_filename, card_info)

    # Show loading message while processing
    loading_message = update.message.reply_text("🔍 Loading...", quote=True)

    # Simulate loading by waiting for a few seconds
    time.sleep(5)

    # Edit loading message to show the generated card information
    update.message.bot.edit_message_text(
        chat_id=update.message.chat_id,
        message_id=loading_message.message_id,
        text=f"✨ Credit Card Generated Successfully!\n\n💳 BIN: {bin_number}\n💰 Amount: {amount}\n\n{card_info}",
        parse_mode='Markdown'
    )

    # Simulate loading by waiting for a few more seconds
    time.sleep(5)

    # Rename the temporary file with the unique name
    unique_filename = '𓆩𝗫𝗲𝗿𝗿𝗼𝘅𓆪「Zone ↯」.txt'
    rename_file(temp_filename, unique_filename)

    # Remove emojis from the file content
    remove_emojis_from_file(unique_filename)

    # Send the card information to the user without emojis
    with open(unique_filename, 'r') as file:
        card_info_no_emojis = file.read()

    update.message.reply_text(card_info_no_emojis)

def generate_card_number(bin_number):
    # Generate the remaining digits of the card number
    card_digits = [random.randint(0, 9) for _ in range(9)]
    card_number = bin_number + ''.join(map(str, card_digits))
    return card_number

def generate_cvv():
    # Generate a random CVV with 3 digits
    cvv = ''.join(str(random.randint(0, 9)) for _ in range(3))
    return cvv

def generate_expiration_date():
    # Generate a random expiration date
    month = random.randint(1, 12)
    year = random.randint(2023, 2028)
    expiration_date = f"{month:02d}/{year}"
    return expiration_date

def save_to_file(filename, content):
    # Save the content to a file
    with open(filename, 'w') as file:
        file.write(content)

def rename_file(old_filename, new_filename):
    # Rename a file
    import os
    os.rename(old_filename, new_filename)

def remove_emojis_from_file(filename):
    # Remove emojis from a file content
    with open(filename, 'r+') as file:
        content = file.read()
        modified_content = remove_emojis(content)
        file.seek(0)
        file.write(modified
