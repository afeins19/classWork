"""OpenCV Project #1 Color Detection (Python)
• Modify blue object detector using HSV and OpenCV to detect both red and blue images (80%)
• If more than one blue object, then display only the largest blue object and display centroid (10%)
• If more than one red object, then display only the largest red object and display centroid (10%)
• Pick good (real world) test cases. Include 5 test cases for red objects and 5 test cases for blue objects
• Include a max of 20% failures ("edge" failures). NOTE: Develop one program to detect both colors
"""

# this program will track a blue object in the HSV Color Space 

# HSV WHEEL IS 180 DEGREES
# HSV type of color represented by (saturation, theta) where r is the saturation elvel and thetat is the angle around the color wheel 
# (170-10) = red, (35-85) = green, (100-130) is blue 
import cv2 as cv 
import numpy as np 


def filterByColor(img, thresh_low, thresh_high):
    # creates masks to filter frame by specified threshold bgr vals
    # convert to hsv
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # create mask to filter between pixel intensity thresholds
    mask = cv.inRange(hsv, thresh_low, thresh_high)

    # img AND mask to filter out none matching pixels 
    res = cv.bitwise_and(img, img, mask=mask)
    return mask 

def getLargestContours(img, min_size):
    # gets centroids and areas of contours and selects largest one
    # setting the threshold pixel intensity >= 150
    ret, filtered_img = cv.threshold(img, 150, 255, cv.THRESH_BINARY)

    # contour detection and selection 
    contours, _ = cv.findContours(filtered_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    if contours:
        largest = max(contours, key=cv.contourArea)
        largest_contour_area = cv.contourArea(largest) 

        if largest_contour_area >= min_size:
            return largest
        
    return None


def indicateObjects(img, contour, color, text):
    # set dimensions of contour and draw onto image
    x, y, w, h = cv.boundingRect(contour)
    cv.rectangle(img, (x,y), (x+w, y+h), color, 2)
    cv.putText(img, f'{text}', (x - 25, y - 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # centroids: code from learnopencv.com (finding moments and calculating centroids)
    M = cv.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])

        # draw the centroid as a small circle
        cv.circle(img, (cx, cy), 5, (255,255,255), -1)
        
    return img 

CAM_LOC = '/dev/video0'

cap = cv.VideoCapture(CAM_LOC)

img_capture = 0

while(True): 
    # frame by frame processing 
    _, frame = cap.read()

    # defining thresholds for colors
    low_b = np.array([110,50,50])
    high_b = np.array([130,255,255])

    # red spans 2 color spaces in hsv space
    low_r1 = np.array([0,150,50])
    high_r1 = np.array([10,255,255])
    low_r2 = np.array([170,150,50])
    high_r2 = np.array([180,255,255])


    # generating filtered images 
    mask_b = filterByColor(frame, low_b, high_b)

    mask_r1 = filterByColor(frame, low_r1, low_r2)
    mask_r2 = filterByColor(frame, low_r2, high_r2)
    
    # ORing r1 and r2 masks to get all red coverage
    mask_r = cv.bitwise_or(mask_r1, mask_r2)

    # finding and plotting largest red and blue objects 
    lc_b = getLargestContours(mask_b, min_size=100)
    lc_r = getLargestContours(mask_r, min_size=100)

    frame = indicateObjects(frame, lc_b, (255,0,0), text="Largest Blue") # blue objects
    frame = indicateObjects(frame, lc_r, (0,0,255), text="Largest Red") # red objects

    cv.imshow('Color Detector',frame)
    
    k= cv.waitKey(5) & 0xFF
    if k== 27: # ascii of spacebar = 27
        cv.destroyAllWindows()
        cap.release()
        break
    
    # capture image with p
    elif k== ord('p'):
        cv.imwrite(f"capture_{str(img_capture)}.png", frame)
        img_capture+=1
        







    

