import numpy as np
import cv2
from utils import shape_title



# load in image
image = cv2.imread('shapes.jpg')
image_copy = image.copy()

# convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply gaussian
#blur = cv2.GaussianBlur(gray, (3, 3), 0)

# apply threshold to image
_, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# dialate image
#dilate = cv2.dilate(threshold, None, iterations=3)

# find contours
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# interate through contours to detect shapes
for contour in contours:
    # calculate perimeter of contour
    perimeter = cv2.arcLength(contour, True)

    # approximate the geometry shape of given contour
    approx = cv2.approxPolyDP(contour, 0.01*perimeter, True)

    # print('Approx is: ', approx)

    # draw approximation on image
    cv2.drawContours(image, [approx], 0, (200, 33, 1), 1)

    # find bounding box of contour, then put shape name on top
    (x, y, w, h) = cv2.boundingRect(approx)

    # print((x, y, w, h))

    # get name of shape based on length of approx
    title = shape_title(len(approx), approx)

    # put text on image
    cv2.putText(image_copy, title, (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 34), 1)

    


print('Length of contours is: ', len(contours))

# show image
cv2.imshow('Original', image_copy)
cv2.imshow('Threshold', threshold)
cv2.imshow('Processed', image)


cv2.waitKey(0)
cv2.destroyAllWindows()
