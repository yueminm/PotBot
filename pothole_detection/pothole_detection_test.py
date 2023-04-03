import cv2
import numpy as np

# Load the image
img = cv2.imread('test_images/test2.jpg')

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a threshold to the image to obtain the black areas
ret, thresh = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY)

# Convert the image to HSV color space
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the range of the pink color in HSV format
lower_pink = np.array([140, 50, 70], dtype='uint8')
upper_pink = np.array([160, 240, 240], dtype='uint8')

# Create a mask with the pink areas
mask_pink = cv2.inRange(img_hsv, lower_pink, upper_pink)

# Combine the masks to obtain the pink areas on black background
mask = cv2.bitwise_and(thresh, mask_pink)

# Calculate the histogram of the pink areas in the image
hist = cv2.calcHist([img_hsv], [0], mask, [256], [0, 256])

# Normalize the histogram
cv2.normalize(hist, hist, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

# Calculate the backprojection of the pink areas in the image
backproj = cv2.calcBackProject([img_hsv], [0], hist, [0, 256], 1)

# Apply a threshold to the backprojection to obtain the pink areas
ret, thresh = cv2.threshold(backproj, 50, 255, cv2.THRESH_BINARY)

# Display the result
cv2.imshow('Pink areas on black background detection with histogram', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
