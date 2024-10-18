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
    target_color = (0, 255, 0)

    # create images
    for sn in range(1, 1 + n_units):

        interpolated_color = get_interpolated_colour(initial_color, target_color, n_units - 1, sn - 1)
        
        # front image
        create_image({
            "img_width": 900,
            "img_height": 1200,
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
            "font_path": "fonts/Ubuntu-Bold.ttf",
            "output_filepath": "output/sn_"+str(sn)+"_back.png",
            "front_background_color": (255, 0, 0),
            "background_color": (255, 255, 255),
            "logo_filepath": 'assets/logo.png',
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

# from https://stackoverflow.com/questions/64034165/how-to-do-linear-interpolation-with-colors
def get_interpolated_colour(initial_color, target_color, number_of_rows, row):
    deltas=[(target_color[i] - initial_color[i])/number_of_rows for i in range(3)]
    interpolated_color=tuple([initial_color[i] + (deltas[i] * row) for i in range(3)])
    return interpolated_color

main()