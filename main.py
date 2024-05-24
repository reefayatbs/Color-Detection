import numpy as np
import cv2 as cv
from util import getLimits
from PIL import Image
from util import colorToBGR


colorDict = {
    "green": [0, 255, 0],
    "blue": [255, 0, 0],
    "yellow": [0, 255, 255],
}

while True:
    color = input("Please enter the target color: ")

    if colorDict.__contains__(color):
        color = colorToBGR(color, colorDict)
        break
    
    print("Color not in System: ")

 
cap = cv.VideoCapture(0)

# Checking to see if the webcam is valid
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Infinite loop of actually running the camera
while True:

    # function that returns boolean of whether frame is read correctly and 
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lowerLim, upperLim = getLimits(color)

    region = cv.inRange(hsvImage, lowerLim, upperLim)

    boundary = Image.fromarray(region)

    boundaryRegion = boundary.getbbox()

    if boundaryRegion is not None:
        x1, y1, x2, y2 = boundaryRegion

        frame = cv.rectangle(frame, (x1,y1), (x2,y2), (0,0,255), 5)

    cv.imshow('Real-Time Footage', frame)

    if cv.waitKey(1) == ord('q'):
        break
 

cap.release()
cv.destroyAllWindows()