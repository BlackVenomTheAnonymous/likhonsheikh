from PIL import Image, ImageDraw, ImageFont

def generate_checkout_image(card_info, amount, receipt_link):
    # Create a black background image
    image = Image.new('RGB', (500, 400), 'black')
    draw = ImageDraw.Draw(image)

    # Set the font and text color
    font = ImageFont.truetype('arial.ttf', 24)
    text_color = (255, 255, 255)

    # Calculate the center position for the text
    text = 'CHARGED'
    text_width, text_height = draw.textsize(text, font)
    text_x = (image.width - text_width) // 2
    text_y = (image.height - text_height) // 2

    # Draw the text on the image
    draw.text((text_x, text_y), text, font=font, fill=text_color)

    # Add styling elements
    flag = '🚩'  # Replace with your random flag
    ip = '192.168.0.1'  # Replace with the generated fake IP
    charged_cards = ', '.join(card_info)  # Replace with the list of charged card numbers
    success_message = '+ Payment Successful (  𓆩𝗫𝗲𝗿𝗿𝗼𝘅𓆪「Zone ↯」)'
    api_name = '𓆩𝗫𝗲𝗿𝗿𝗼𝘅𓆪'
    support_message = '+ Support!  𓆩𝗫𝗲𝗿𝗿𝗼𝘅𓆪「Zone ↯」'

    # Add the styled text on the image
    draw.text((20, 50), f'• CHARGED {flag} IP: {ip}', font=font, fill=text_color)
    draw.text((20, 100), f'#CHARGED: {charged_cards}', font=font, fill=text_color)
    draw.text((20, 150), success_message, font=font, fill=(0, 255, 0))  # Green color
    draw.text((20, 200), f'† Amount: {amount}', font=font, fill=text_color)
    draw.text((20, 250), '+ Receipt:', font=font, fill=text_color)
    draw.text((200, 250), receipt_link, font=font, fill=text_color)
    draw.text((20, 300), f'† API BY: {api_name}', font=font, fill=text_color)
    draw.text((20, 350), support_message, font=font, fill=(255, 255, 255))  # White color

    # Add a random checkmark emoji for 15 seconds
    checkmark_emojis = ['✅', '✔️', '🟢', '🌟']  # Add more checkmark emojis if desired
    checkmark = random.choice(checkmark_emojis)
    draw.text((400, 20), checkmark, font=font, fill=(255, 255, 255))  # White color

    # Draw a line beneath the button text
    button_x, button_y = 200, 250
    button_text = receipt_link
    button_text_width, button_text_height = draw.textsize(button_text, font)
    line
