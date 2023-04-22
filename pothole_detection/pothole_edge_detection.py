import cv2
import numpy as np
# from tensorflow.keras.preprocessing import image

# Read the original image
img = cv2.imread(
    '/Users/helenmao/Desktop/Pothole1.png')
# img = image.img_to_array(img, dtype='uint8')

# Display original image
# cv2.imshow('original image',img)

rWidth, rHeight = 288, 215
dim = (rWidth, rHeight)
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('resized image', img)

# First blur
img_blur = cv2.GaussianBlur(img, (7,7), 0) 
# kernel = np.ones((3, 3), np.uint8)
# img_blur = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("1st blur",img_blur)

# Convert to graycsale
img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale",img_gray)

# Thresholding to binary 
ret, img_thresh = cv2.threshold(img_gray, 95, 255, cv2.THRESH_BINARY)
# img_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                            cv2.THRESH_BINARY, 11, 2)
cv2.imshow("thresholded", img_thresh)

# Second blur
img_blur2 = cv2.medianBlur(img_thresh, 15)
# kernel = np.ones((15, 15), np.uint8)
# img_blur2 = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)
cv2.imshow("2nd blur",img_blur2)


# Sobel Edge Detection
# kernel = 11
# sobelx = cv2.Sobel(src=img_blur2, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=kernel) # Sobel Edge Detection on the X axis
# sobely = cv2.Sobel(src=img_blur2, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=kernel) # Sobel Edge Detection on the Y axis
# sobelxy = cv2.Sobel(src=img_blur2, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=kernel) # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images
# cv2.imshow('Sobel X', sobelx)
# cv2.waitKey(0)
# cv2.imshow('Sobel Y', sobely)
# cv2.waitKey(0)
# cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
# cv2.waitKey(0)
 
# Canny Edge Detection
img_edges = cv2.Canny(image=img_blur2, threshold1=10, threshold2=100, L2gradient = True) # Canny Edge Detection
cv2.imshow('Canny Edge Detection', img_edges)

# Third blur
# img_blur3 = cv2.medianBlur(img_edges, 15)
kernel = np.ones((5, 5), np.uint8)
img_blur3 = cv2.morphologyEx(img_edges, cv2.MORPH_CLOSE, kernel)
cv2.imshow("3rd blur", img_blur3)

# Find contours and find total area
cnts = cv2.findContours(img_blur3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
area = []
area_max = 0
c_max = cnts[0]
for c in cnts:
    # print(cv2.contourArea(c))
    area_curr = cv2.contourArea(c)
    area.append(cv2.contourArea(c))
    if area_curr > area_max:
        area_max = area_curr
        c_max = c

cv2.drawContours(img,[c_max], 0, (0,255,0), 2)
print("pothole area is the max area = %i pixels" %max(area))
cv2.imshow('draw contour', img)
cv2.waitKey(0)
cv2.destroyAllWindows()