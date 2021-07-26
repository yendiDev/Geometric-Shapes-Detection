import cv2
import numpy as np

def shape_title(corners, approx):
    if int(corners) == 3:
        return 'Triangle'

    elif int(corners) == 4:
        # choose whether shape is rectangle or square
        (x, y, w, h) = cv2.boundingRect(approx)

        # calculate width and height
        # width = 

        return 'Rectangle'

    elif int(corners) == 5:
        return 'Pentagon'

    else: 
        return 'Circle'
