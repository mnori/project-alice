import cv2
import numpy as np
import textwrap
import PIL
from PIL import Image
from matplotlib import pyplot as plt
from PIL import ImageFont
from PIL import ImageDraw

font_size =  140
config = {
    "margin_left": 90,
    "margin_top": 50,
    "font_size": font_size,
    "line_height": 1.3 * font_size,
    "stroke_width": 15,
    "wordwrap_width": 34 / (font_size / 100),
    "background_color": (255, 0, 0),
    "stroke_darkness": 0.5,
    "text_color": (255, 255, 255),  # White color
    "font_path": "fonts/Ubuntu-Bold.ttf",
    "img_width": 1800,
    "img_height": 2400,
    "image_file_name": 'output/firstone.png'
}

def main():
    whole_text = "! Important information     ! Trigger warning            ! Stay safe "
    apply_text(whole_text)

def apply_text(whole_text):
    stroke_fill = (
        int(config["background_color"][0] * config["stroke_darkness"]), 
        int(config["background_color"][1] * config["stroke_darkness"]), 
        int(config["background_color"][2] * config["stroke_darkness"]))
    wrapped_text = textwrap.wrap(whole_text, config["wordwrap_width"])
    font = ImageFont.truetype(config["font_path"], config["font_size"])
    image = np.zeros((config["img_height"], config["img_width"], 3), dtype=np.uint8)
    image[:] = config["background_color"]
    image_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(image_pil)

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

    image_with_text = np.array(image_pil)  #
    image_with_text = Image.fromarray(image_with_text)
    image_with_text.save(config["image_file_name"])

main()