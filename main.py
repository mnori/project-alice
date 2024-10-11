import numpy
import cv2
from PIL import Image

print("Hello World")

# Make image using set width and height
width = 1800
height = 2400
blank_image = numpy.zeros((height, width, 3), numpy.uint8)

# Turn the whole image red
blank_image[:] = (255, 0, 0)

# Show image object class name
print(blank_image.__class__.__name__) 

# Define the file name to save the image
image_file_name = 'output/firstone.png'

# Convert the NumPy array to an image object
image = Image.fromarray(blank_image)

# Save the image object to a PNG file
image.save(image_file_name)
