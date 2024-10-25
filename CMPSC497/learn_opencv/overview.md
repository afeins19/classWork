# Some Important OpenCV functions 

### Reading in an Image
**NOTE:** the color channel order is (B,G,R) not (R,G,B)
- `imread(image, formate_code)` - reads an image from a file 
    - `cv.IMREAD_UNCHANGED` - used for images with a transparency channel
    - `cv.IMREAD_GRAYSCALE` - used for converting to grayscale
    - `cv.IMREAD_COLOR` - this is the default 

### Displaying and Writing an Image 
- `imshow('window_title', image)` - this will display the image in a window titled 'window_title'

- imwrite(filename, image) - saves an image to a file

