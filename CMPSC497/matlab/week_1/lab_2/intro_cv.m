% Lab 2 - Intro to Computer Vision 

% 1. loading in image 
im = imread('peppers.png'); 

% 2. displaying image and attributes 
imshow(im)
im_size = size(im)

% 3. using imtool to display two separate pixel regions
imtool(im) 

% 4. separating plane of the RGB image and displaying 
im_red = im(:,:,1);
im_green = im(:,:,2);
im_blue = im(:,:,3);

imshow(im_red) 
imshow(im_green) 
imshow(im_blue) 

% 5. Converting image to grayscale 
im_gray = rgb2gray(im);
imshow(im_gray)

% 6. min, max, avg pixel values of grayscale 
im_min = min(min(im_gray))
im_max = max(max(im_gay))
im_avg = mean(mean(im_gray))

% 7. historgyam 
imhist(im_gray)
xlabel = 'Pixel Intensity'
ylabel = 'Count of Pixels'