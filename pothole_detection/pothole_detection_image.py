from turtle import end_fill
import numpy as np
import cv2

img = cv2.imread('test_images/test5.jpg')
height = len(img)
width = len(img[0])
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_purple = np.array([140, 50, 70], dtype='uint8')
upper_purple = np.array([160, 240, 240], dtype='uint8')

mask = cv2.inRange(img_hsv, lower_purple, upper_purple)
if not any(255 in x for x in mask):
    print('No potholes in the view')
else:
    print('Pothole detected')
    edges = np.where(mask==255)
    closest_point = np.where(edges[0]==edges[0].max())
    i_closest = closest_point[0][0]
    [row, col] = [edges[0][i_closest], edges[1][i_closest]]
    print(row, col)

img_filtered = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("red color detection", img_filtered)

img_processed = cv2.circle(img, (col, row), 10, (0, 255, 0), 5)
cv2.imshow('processed image', img_processed)
cv2.waitKey(0)

