import os
import colorsys
import glob
import cv2
import numpy as np
import textwrap
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

font_size = 70
n_units = 32

def main():

    # clear output folder
    files = glob.glob('output/*')
    for f in files:
        os.remove(f)

    initial_color = (255, 0, 0)
    target_color = (255, 255, 0)

    # create images
    for sn in range(1, 1 + n_units):
        interpolated_color = get_rainbow_interpolated_colour(n_units - 1, sn - 1)
        print("Interpolated color: ", interpolated_color)

        # front image
        create_image({
            "img_width": 900, # 18mm / 2
            "img_height": 1200, # 24mm / 2
            "logo_size": 700,
            "font_path": "fonts/Ubuntu-Bold.ttf",
            "output_filepath": "output/sn_"+str(sn)+"_front.png",
            "background_color": interpolated_color,
            "logo_filepath": 'assets/warning.png',
            "text_color": (255, 255, 255),
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
        # back image
        create_image({
            "img_width": 900,
            "img_height": 1200,
            "logo_size": 820,
            "font_path": "fonts/Ubuntu-Bold.ttf",
            "output_filepath": "output/sn_"+str(sn)+"_back.png",
            "front_background_color": (255, 0, 0),
            "background_color": (255, 255, 255),
            "logo_filepath": 'assets/logo_alt.png',
            "text_color": (255, 255, 255),
            "margin_left": 45,
            "margin_top": 1000,
            "font_size": font_size,
            "wordwrap_width": 25,
            "line_height": 1.3 * font_size,
            "stroke_width": 8,
            "stroke_darkness": 0.5,
            "message": \
                "Series 1                 "+\
                "SN "+str(sn)+"/"+str(n_units)+" \n" 
        })

def create_image(config):
    image = np.zeros((config["img_height"], config["img_width"], 3), dtype=np.uint8)
    image[:] = config["background_color"]
    main_image = Image.fromarray(image)

    draw_image(main_image, config)
    
    draw = ImageDraw.Draw(main_image)
    draw_text(draw, config)

    image_with_text = np.array(main_image)
    image_with_text = Image.fromarray(image_with_text)
    image_with_text.save(config["output_filepath"])

def draw_image(main_image, config):
    img = Image.open(config["logo_filepath"])
    img = img.resize((config["logo_size"], config["logo_size"]))
    offset = int((config["img_width"] - config["logo_size"]) / 2)
    main_image.paste(img, (offset, offset), img)

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

def get_rainbow_interpolated_colour(n_colours, position):
    position = (position / 6) * 5 # chop of purple to red part
    hue = (position / n_colours) * 255
    saturation = 255
    value = 255
    hsv = (hue, saturation, value)
    rgb = colorsys.hsv_to_rgb(hsv[0] / 255, hsv[1] / 255, hsv[2] / 255)
    return (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

main()