import cv2 as cv
import numpy as np
import math

def detectLines(img_loc):
    # loading image 
    img = cv.imread(img_loc, cv.IMREAD_GRAYSCALE) # convert to gray

    canny = cv.Canny(img, 50, 200, None, 3)

    # save edges to be displayed later im final image 
    img_edges = cv.cvtColor(canny, cv.COLOR_GRAY2BGR)
    
    # apply hough transform 
    lines_detected = cv.HoughLines(canny, 1, np.pi /180, 150, None, 0, 0)

    # constructing accumulator matrix
    accum = []

    if lines_detected is not None: 
        # make and draw lines 
        for i in range(len(lines_detected)): 
            rho_cur = lines_detected[i][0][0]
            theta_cur = lines_detected[i][0][1]

            # get x,y coordinates of each point in cartesian space
            a = math.cos(theta_cur)
            b= math.sin(theta_cur)     
            x0 = a * rho_cur
            y0 = b * rho_cur

            # store values 
            accum.append((rho_cur, theta_cur))

            # generate points and plot 
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv.line(img_edges, pt1, pt2, (0,0,255), 3, cv.LINE_AA)

        cv.imshow("Detected Lines: {str(len(lines))}", img)

if __name__ == "__main__":
    IMG_LOC = '/home/aaron/Projects/classWork/CMPSC497/learn_opencv/hw_labs/hough_line_detection/test/highway.jpg'
    detectLines(IMG_LOC)