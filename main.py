import cv2
import numpy as np
import textwrap
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

font_size = 70

def main():
    create_image({
        "img_width": 900,
        "img_height": 1200,
        "font_path": "fonts/Ubuntu-Bold.ttf",
        "output_filepath": 'output/front.png',
        "background_color": (255, 0, 0),
        "logo_filepath": 'assets/warning.png',
        "text_color": (255, 255, 255),  # White color
        "margin_left": 45,
        "margin_top": 900,
        "font_size": font_size,
        "wordwrap_width": 25,
        "line_height": 1.3 * font_size,
        "stroke_width": 8,
        "stroke_darkness": 0.5,
        "message": \
            "! Trigger warning         "+\
            "Important information     "+\
            "Stay safe "
    })
    create_image({
        "img_width": 900,
        "img_height": 1200,
        "font_path": "fonts/Ubuntu-Bold.ttf",
        "output_filepath": 'output/back.png',
        "front_background_color": (255, 0, 0),
        "background_color": (255, 255, 255),
        "logo_filepath": 'assets/logo.png',
        "text_color": (255, 255, 255),  # White color
        "margin_left": 45,
        "margin_top": 1000,
        "font_size": font_size,
        "wordwrap_width": 25,
        "line_height": 1.3 * font_size,
        "stroke_width": 8,
        "stroke_darkness": 0.5,
        "message": \
            "Series 1                 "+\
            "SN 1/32 \n" 
    })

def create_image(config):
    image = np.zeros((config["img_height"], config["img_width"], 3), dtype=np.uint8)
    image[:] = config["background_color"]
    main_image = Image.fromarray(image)

    draw_image(main_image, config["logo_filepath"])

    draw = ImageDraw.Draw(main_image)
    draw_text(draw, config)

    image_with_text = np.array(main_image)
    image_with_text = Image.fromarray(image_with_text)
    image_with_text.save(config["output_filepath"])

def draw_image(main_image, image_filepath):
    img = Image.open(image_filepath)
    img = img.resize((700, 700))
    main_image.paste(img, (100, 100), img)

def draw_text(draw, config):
    stroke_fill = (
        int(config["background_color"][0] * config["stroke_darkness"]), 
        int(config["background_color"][1] * config["stroke_darkness"]), 
        int(config["background_color"][2] * config["stroke_darkness"]))

    wrapped_text = textwrap.wrap(config["message"], config["wordwrap_width"])
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

main()