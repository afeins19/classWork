# opening and displaying an image in OpenCV 

import cv2 as cv 

IMG_LOC = 'Photos/cat.jpg'
CAMERA_LOC = '/dev/video0'

image_original = cv.imread(IMG_LOC) # read in the image
image_grayscale = cv.imread(IMG_LOC, cv.IMREAD_GRAYSCALE)

cv.imshow(IMG_LOC, image_original)  # display image
cv.imshow(IMG_LOC, image_grayscale)  # display image
cv.waitKey(0)              # set exit key to '0'
cv.destroyAllWindows() 

# splitting channels 
b,g,r = cv.split(image_original)

# equivalent to these operations
b=image_original[:,:,0]
g=image_original[:,:,1]
r=image_original[:,:,2]

# image specifications 
dimensions = image_original.shape 
height = image_original.shape[0]
width = image_original.shape[1]
channels = image_original.shape[2]

# converting images (bgr -> rgb and rgb -> bgr)
rgb = cv.cvtColor(image_original, cv.COLOR_BGR2RGB)
gray = cv.cvtColor(image_original, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(image_original, cv.COLOR_BGR2HSV)

# converting images to binary 
gray = cv.cvtColor(image_original, cv.COLOR_BGR2GRAY)

# BW is the binary image, 127 is threshold, max=255
(thresh, BW) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

# Displaying Video from the webcam 
print("Starting video feed...")
cap = cv.VideoCapture(CAMERA_LOC) # default webcam

# capturing frame by frame 
while(True):
    ret, frame = cap.read()

    cv.imshow(CAMERA_LOC,frame)
    if cv.waitKey(1) & 0xFF==ord('q'): # hex for 255
        break

cap.release()
cv.destroyAllWidnows() 

# Dilation and Erosion 
img = cv.imread('j.png', 0)