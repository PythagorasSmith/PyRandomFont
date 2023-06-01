import os
import random
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter

# Define the text for the PDF
text = "\"There are two types of people in this world...\""

# Specify the directory containing the font files
font_directory = 'fonts'

# Register all TTF fonts in the directory
font_paths = [os.path.join(font_directory, file) for file in os.listdir(font_directory) if file.endswith('.ttf')]
font_names = []
for i, font_path in enumerate(font_paths):
    font_name = f'font{i:02d}'  # Use sequential numbering for font names
    font_names.append(font_name)
    pdfmetrics.registerFont(TTFont(font_name, font_path))

# Create a PDF canvas
c = canvas.Canvas("documents/output.pdf", pagesize=letter)

# Set the font size
font_size = 11

# Set the starting position
x, y = 50, 700

# Iterate over each character in the text
for char in text:
    # Select a random font for the character
    random_font = random.choice(font_names)

    # Set the font and font size
    c.setFont(random_font, font_size)

    # Draw the character on the canvas
    c.drawString(x, y, char)

    # Update the x-position for the next character
    x += font_size - 2  # adjust for kerning

# Save and close the PDF
c.save()
