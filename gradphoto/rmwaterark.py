import numpy as np
import cv2 as cv 

img_path = 'gradphoto.jpeg'

im = cv.imread(img_path)

# Define thresholds
channel_threshold = 10  # Max difference between R, G, and B
value_range = (100, 200)  # Range for pixel values

# Calculate absolute differences between channels
diff_rg = np.abs(image[:, :, 0] - image[:, :, 1])  # Red and Green
diff_gb = np.abs(image[:, :, 1] - image[:, :, 2])  # Green and Blue
diff_rb = np.abs(image[:, :, 0] - image[:, :, 2])  # Red and Blue

# Check if the pixel values are within the specified range
within_value_range = (
    (image[:, :, 0] >= value_range[0]) & (image[:, :, 0] <= value_range[1]) &
    (image[:, :, 1] >= value_range[0]) & (image[:, :, 1] <= value_range[1]) &
    (image[:, :, 2] >= value_range[0]) & (image[:, :, 2] <= value_range[1])
)

# Check if the differences between channels are within the threshold
within_channel_range = (diff_rg <= channel_threshold) & (diff_gb <= channel_threshold) & (diff_rb <= channel_threshold)

# Combine both conditions
mask = within_value_range & within_channel_range

# Convert the mask to uint8 format
mask_uint8 = mask.astype(np.uint8) * 255

# Remove the matching pixels by setting them to black (or another color)
result = image.copy()
result[mask] = [0, 0, 0]  # Replace with black; modify this color as needed

# Save the results
cv2.imwrite('mask_removed_pixels.jpeg', result)