import cv2
import numpy as np
import textwrap
import PIL
from PIL import Image
from matplotlib import pyplot as plt
from PIL import ImageFont
from PIL import ImageDraw

def main():
    whole_text = "! Important information     ! Trigger warning            ! Stay safe "
    apply_text(whole_text)

def apply_text(whole_text):
    margin_left = 90
    margin_top = 50
    font_size = 140
    stroke_width = 15
    wordwrap_width = 34 / (font_size / 100)
    background_color = (255, 0, 0)    
    stroke_darkness = 0.5
    stroke_fill = (
        int(background_color[0] * stroke_darkness), 
        int(background_color[1] * stroke_darkness), 
        int(background_color[2] * stroke_darkness))
        
    text_color = (255, 255, 255)  # White color
    font_path = "fonts/Ubuntu-Regular.ttf"
    img_width = 1800
    img_height = 2400
    image_file_name = 'output/firstone.png'

    font = ImageFont.truetype(font_path, font_size)
    image = np.zeros((img_height, img_width, 3), dtype=np.uint8)  # Example image
    image[:] = background_color
    image_pil = Image.fromarray(image)  # Convert OpenCV image to PIL image
    draw = ImageDraw.Draw(image_pil)
    wrapped_text = textwrap.wrap(whole_text, wordwrap_width)

    line_num = 0
    for line in wrapped_text:
        line_height = font_size
        coord = (margin_left, margin_top + (line_num * line_height))
        draw.text(
            coord, 
            line, 
            font=font, 
            fill=text_color,
            stroke_width=stroke_width,
            stroke_fill=stroke_fill)
        line_num += 1

    image_with_text = np.array(image_pil)  # Convert PIL image back to OpenCV image

    # Convert the NumPy array to an image object
    image_with_text = Image.fromarray(image_with_text)

    # Save the image object to a PNG file
    image_with_text.save(image_file_name)

main()