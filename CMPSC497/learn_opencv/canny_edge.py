# using canny edge detection on the image 

import numpy as np 
import cv2  
from matplotlib import pyplot as plt

img = cv2.imread('Photos/cats.jpg',  0) # 0 -> grayscale conversion
IMG_LOC = 'Photos/cats.jpg'

# # applying canny edge detection
# edges = cv.Canny(img, 100, 200) # find the edges

# # noise reduction with gaussian blur 
# blur = cv.GaussianBlur(img, [5,5], 0)

# # plotting edges 
# plt.subplot(121), plt.imshow(blur, cmap='gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])

# plt.subplot(122), plt.imshow(edges, cmap='gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()


def callback(x):
    pass  # This is needed as a placeholder for trackbar callback

# Read the image as grayscale
img = cv2.imread(IMG_LOC, 0)

# Create a window with the name 'image'
cv2.namedWindow('image')

# Create trackbars for lower and upper threshold adjustments
cv2.createTrackbar('L', 'image', 0, 255, callback)  # Lower threshold trackbar
cv2.createTrackbar('U', 'image', 0, 255, callback)  # Upper threshold trackbar

while True:
    # Get current positions of the trackbars
    l = cv2.getTrackbarPos('L', 'image')
    u = cv2.getTrackbarPos('U', 'image')
    
    # Apply Canny edge detection with dynamic thresholds
    canny = cv2.Canny(img, l, u)
    
    # Display the original image and the Canny edge side by side
    numpy_horizontal_concat = np.concatenate((img, canny), axis=1)
    cv2.imshow('image', numpy_horizontal_concat)
    
    # Exit when 'ESC' is pressed
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # ESC key
        break

# Close all windows
cv2.destroyAllWindows()