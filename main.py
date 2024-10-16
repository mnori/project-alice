import cv2
import numpy as np
import textwrap
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

font_size =  70
config = {
    "img_width": 900,
    "img_height": 1200,
    "font_path": "fonts/Ubuntu-Bold.ttf",
    "image_file_name": 'output/firstone.png',
    "background_color": (255, 0, 0),
    "text_color": (255, 255, 255),  # White color
    "margin_left": 45,
    "margin_top": 900,
    "font_size": font_size,
    "wordwrap_width": 25,
    "line_height": 1.3 * font_size,
    "stroke_width": 8,
    "stroke_darkness": 0.5
}

def main():
    create_image()

def create_image():
    image = np.zeros((config["img_height"], config["img_width"], 3), dtype=np.uint8)
    image[:] = config["background_color"]
    main_image = Image.fromarray(image)
    draw = ImageDraw.Draw(main_image)

    draw_text(draw)
    draw_logo(main_image)

    image_with_text = np.array(main_image)
    image_with_text = Image.fromarray(image_with_text)
    image_with_text.save(config["image_file_name"])

def draw_text(draw):
    whole_text = \
        "! Important information     "+\
        "! Trigger warning           "+\
        "! Stay safe "

    stroke_fill = (
        int(config["background_color"][0] * config["stroke_darkness"]), 
        int(config["background_color"][1] * config["stroke_darkness"]), 
        int(config["background_color"][2] * config["stroke_darkness"]))

    wrapped_text = textwrap.wrap(whole_text, config["wordwrap_width"])
    font = ImageFont.truetype(config["font_path"], config["font_size"])
    line_num = 0
    for line in wrapped_text:
        coord = (config["margin_left"], config["margin_top"] + (line_num * config["line_height"]))
        draw.text(
            coord, 
            line, 
            font=font, 
            fill=config["text_color"],
            stroke_width=config["stroke_width"],
            stroke_fill=stroke_fill)
        line_num += 1

def draw_logo(draw):
    # img = Image.open("assets/anonymous_emblem.png")
    img = Image.open("assets/warning.png")
    img = img.resize((700, 700))
    draw.paste(img, (100, 100), img)

main()