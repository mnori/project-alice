import cv2
import numpy as np
import textwrap
import PIL
from PIL import Image
from matplotlib import pyplot as plt
from PIL import ImageFont
from PIL import ImageDraw

def apply_text(whole_text):

    print("Hello World")

    font_path = "fonts/Ubuntu-Regular.ttf"
    font_size = 100

    font = ImageFont.truetype(font_path, font_size)
    # font_height = font.getsize("A")[1]  # Calculate the height using a sample character
    font_height = 24
    image = np.zeros((1800, 2400, 3), dtype=np.uint8)  # Example image
    image[:] = (255, 0, 0) 

    text = "Hello, World!"
    color = (255, 255, 255)  # White color
    position = (50, 50)  # Position to draw the text

    image_pil = Image.fromarray(image)  # Convert OpenCV image to PIL image
    draw = ImageDraw.Draw(image_pil)
    
    wordwrap_width = 36
    wrapped_text = textwrap.wrap(whole_text, wordwrap_width)

    

    line_num = 0
    for line in wrapped_text:
        text_size = 2.5
        thickness = 3
        margin_left = 50
        margin_top = 150
        line_height = 120
        # font = cv2.FONT_HERSHEY_SIMPLEX
        coord = (margin_left + 10, margin_top + (line_num * line_height))

        draw.text(coord, line, font=font, fill=color)

        line_num += 1
        

    #     # cv2.putText(label_image, line,coord, cv2.FONT_HERSHEY_COMPLEX, text_size, (0,0,0), 16, cv2.LINE_AA)
    #     # cv2.putText(label_image, line,coord, cv2.FONT_HERSHEY_COMPLEX, text_size, (255,255,255), 4, cv2.LINE_AA)

    


    image_with_text = np.array(image_pil)  # Convert PIL image back to OpenCV image

    # cv2.imshow("Image with Text", image_with_text)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Define the file name to save the image
    image_file_name = 'output/firstone.png'

    # Convert the NumPy array to an image object
    image_with_text = Image.fromarray(image_with_text)

    # Save the image object to a PNG file
    image_with_text.save(image_file_name)

    


# # Make image using set width and height
# width = 1800
# height = 2400
# label_image = numpy.zeros([height, width, 3], dtype=numpy.uint8)

# # Turn the whole image red
# # It's RGB when it gets saved as a file, but BGR displayed in a window using cv2.imshow
# label_image[:] = (255, 0, 0) 

whole_text = 'You are wondering: "what on earth is this thing?" Let us explain. '
whole_text += 'Important information can be found within this device, information that requires a trigger warning. '
whole_text += 'We are bringing this information to you in peace to warn you about a threat in the local area. '
whole_text += 'This device will not harm your computer. '
whole_text += 'Along with the main cache of information within, we have included a collectable NFT unique to this object, which may gain value in the future. '
whole_text += 'We invite you to consider the information and evidence we are providing as it will help protect you and and your loved ones. '
whole_text += 'Stay safe. '

apply_text(whole_text)
# # print(wrapped_text.__class__.__name__)



# write_text(1, wrapped_text)

# write_text(1, 'Trigger warning.')
# write_text(2, 'Important information enclosed.')
# write_text(3, 'Unique NFT included.')
# write_text(4, 'This will not harm your computer.')
# write_text(5, 'The content on this device will instead warn you about a threat in the local area.')
# write_text(6, 'We are bringing this to you in peace.')


# cover_text = 'Trigger warning.\n'
# cover_text += 'Important information enclosed.\n'




# cv2.imwrite(path + 'pillar_text.jpg', label_image)

# Show image object class name
# print(label_image.__class__.__name__) 

# font
# font = cv2.FONT_HERSHEY_SIMPLEX

# org
# org = (50, 50)

# fontScale
# fontScale = 1
 

# # Line thickness of 2 px
# thickness = 2
 
# # Using cv2.putText() method
# # label_image = cv2.putText(label_image, 'OpenCV', org, font, 
# #                    fontScale, color, thickness, cv2.LINE_AA)

# # window_name = 'Label Image'
# # cv2.imshow(window_name, label_image) 
# # cv2.waitKey(0)

# # plt.show()



