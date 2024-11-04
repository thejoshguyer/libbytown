from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
import random
from io import BytesIO

# Load data from CSV file
with open('towns.csv', 'r') as f:
    data = [line.split(',') for line in f.readlines()]

# Initialize Flask app
app = Flask(__name__)

# Route to generate image
@app.route('/')
def generate_image():
    # Generate random text
    text = random.choice(data)[0]

    # Load London Underground font
    font_size = 50
    font = ImageFont.truetype('Cabin-Regular.ttf', size=font_size)

    # Load London Underground image
    image = Image.open('Underground-no-text.png')

    # Generate image
    draw = ImageDraw.Draw(image)

    # Calculate position of text
    text_bbox = font.getmask(text).getbbox()
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (image.width - text_width) / 2
    y = ((image.height - text_height) / 2) - 10

    # Draw text
    draw.text((x, y), text, fill='#FFFFFF', font=font)

    # Convert image to bytes
    img_bytes = BytesIO()
    image.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    # Return image
    return send_file(img_bytes, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
