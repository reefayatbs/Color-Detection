import numpy as np
import cv2 as cv



def getLimits(color):
    
    c = np.uint8([[color]])

    hsvC = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    lowLim = hsvC[0][0][0] - 10, 100, 100

    highLim = hsvC[0][0][0] + 10, 255, 255

    lowLim = np.array(lowLim, dtype=np.uint8)
    highLim = np.array(highLim, dtype = np.uint8)

    return lowLim, highLim


def colorToBGR(color, dict):
    return dict.get(color)


