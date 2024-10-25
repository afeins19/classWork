
# Applying Dilation and Erosion over an image
# using open and close to edit/process images 
import cv2 as cv 
import numpy as np 

IMG_LOC = 'Photos/j.png'
CAMERA_LOC = '/dev/video0'

img = cv.imread(IMG_LOC, 0) # 0 indicates default bgr read in of image
kernel = np.ones((10,10), np.uint8) # 10x 10 matrix of ones 

#cv.imshow(IMG_LOC, img)
#cv.waitKey(0)              # set exit key to '0'
#cv.destroyAllWindows() 

# applying erosion and dilation 
erosion = cv.erode(img, kernel, iterations=1)
cv.imshow('[ERODED] {IMG_LOC}', erosion)
cv.waitKey(0)              # set exit key to '0'


dilation = cv.dilate(img, kernel, iterations=1)
cv.imshow('[DILATED] {IMG_LOC}', dilation)
cv.waitKey(0)              # set exit key to '0'


# opening and closing 

# opening = erosion -> dilation
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
cv.imshow('[OPEN] {IMG_LOC}', opening)
cv.waitKey(0)              # set exit key to '0'


# closing = dilation -> erosion 
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
cv.imshow('[CLOSE] {IMG_LOC}', closing)
cv.waitKey(0)              # set exit key to '0'

cv.destroyAllWindows() 

# creating structuring elements 
struct = cv.getStructuringElement(cv.MORPH_RECT, (5,5))
print('rectangle:\n', str(struct))

struct = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
print('elipse:\n',str(struct))

