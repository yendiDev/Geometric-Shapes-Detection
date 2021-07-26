import cv2 as cv
import numpy as np

# load image
image = cv.imread('shapes.jpg')

# extract part of image
new_image = image[100:200, 400:600]

# save new image
cv.imwrite('image_part.jpg', new_image)