import numpy
import cv2

print("Hello World")

width = 1800
height = 2400

blank_image = numpy.zeros((height, width, 3), numpy.uint8)

cv2.imshow("A New Image", blank_image)
cv2.waitKey(0)


# Create a 1800 x 2400 pixel image using ImageMagick

# Fill it with a solid color

# Add some text to the image

