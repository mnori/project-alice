import os
import colorsys
import glob
import cv2
import numpy as np
import textwrap
import PIL
import math
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

font_size = 70
n_units = 32

def main():
    clear_output_folder()
    create_label_images()
    combine_label_images()

def clear_output_folder():
    files = glob.glob('output/*')
    for f in files:
        os.remove(f)

def create_label_images():
    
    # create images
    for sn in range(1, 1 + n_units):
        interpolated_color = get_rainbow_interpolated_colour(n_units - 1, sn - 1)
        print("Interpolated color: ", interpolated_color)

        # front image
        create_label_image({
            "img_width": 900, # 18mm / 2
            "img_height": 1200, # 24mm / 2
            "logo_size": 820,
            "font_path": "assets/fonts/Ubuntu-Bold.ttf",
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
        create_label_image({
            "img_width": 900,
            "img_height": 1200,
            "logo_size": 820,
            "font_path": "assets/fonts/Ubuntu-Bold.ttf",
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

def create_label_image(config):
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

def combine_label_images():
    # see table for deets
    lr_margin = 600
    tb_margin = 750
    gap_between = 150
    label_width = 900
    label_height = 1200
    labels_per_row = 9
    combined_width = \
        lr_margin * 2 + \
        (label_width * labels_per_row) + \
        (gap_between * (labels_per_row - 1))
    n_rows = int(np.ceil(n_units / labels_per_row)) * 2
    combined_height = \
        tb_margin * 2 + \
        (label_height * n_rows) + \
        (gap_between * (n_rows - 1))
    combined_np = np.zeros((combined_height, combined_width, 3), dtype=np.uint8)
    combined_np[:] = (255, 255, 255)
    combined_save = Image.fromarray(combined_np).convert("RGBA")

    # Paste images here
    for sn in range(1, 1 + n_units):
        ## get front, paste
        snm1 = sn - 1
        x_position = snm1 % 9
        y_position = math.floor(snm1 / 9)

        label_img = Image.open("output/sn_"+str(sn)+"_front.png").convert("RGBA")
        offset = (
            lr_margin + (x_position * (label_width + gap_between)), 
            tb_margin + (y_position * (label_height + gap_between)))
        combined_save.paste(label_img, offset, label_img)
    
    combined_save.save("output/combined.png")

main()