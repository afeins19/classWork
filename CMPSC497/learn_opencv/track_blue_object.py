# this program will track a blue object in the HSV Color Space 

# HSV WHEEL IS 180 DEGREES
# HSV type of color represented by (saturation, theta) where r is the saturation elvel and thetat is the angle around the color wheel 
# (170-10) = red, (35-85) = green, (100-130) is blue 
import cv2 as cv 
import numpy as np 

CAM_LOC = '/dev/video0'

cap = cv.VideoCapture(CAM_LOC)

while(True): 
    # frame by frame processing 
    _, frame = cap.read()

    # convert BGR -> HSV 
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # (np.array([B,G,R]))
    # set the blue range in HSV (threshold)
    low_b = np.array([110,50,50])
    high_b = np.array([130,255,255])

    # creating mask using ranges 
    mask = cv.inRange(hsv, lowerb=low_b, upperb=high_b)

    # perform bitwise AND operation with original image 
    res = cv.bitwise_and(frame, frame, mask=mask)
    # cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)

    k= cv.waitKey(5) & 0xFF
    if k== 27: # ascii of spacebar = 27
        break
        cv.destroyAllWindows()

    