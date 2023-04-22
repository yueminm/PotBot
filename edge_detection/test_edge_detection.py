# import cv2

# cap = cv2.VideoCapture(
#     "/Users/helenmao/Downloads/WIN_20230421_14_27_48_Pro.mp4")

# pothole_threshold = 150

# while cap.isOpened():
#     _, frame = cap.read()
    
#     rWidth, rHeight = 288, 215
#     dim = (rWidth, rHeight)
#     frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Apply a Gaussian blur to the grayscale image
#     blurred = cv2.GaussianBlur(gray, (5, 5), 0)

#     # Detect edges using the Canny edge detector
#     edges = cv2.Canny(blurred, 50, 150)

#     # Threshold the edge image to find potholes
#     potholes = cv2.threshold(edges, pothole_threshold,
#                              255, cv2.THRESH_BINARY)[1]

#     # Count the number of pixels in the pothole image
#     pothole_pixels = cv2.countNonZero(potholes)
#     print(pothole_pixels)

#     # Check if the robot has moved onto a pothole
#     if pothole_pixels > 100:
#         print("Pothole detected!")

#     # Display the resulting images
#     # cv2.imshow('Edges', edges)
#     cv2.imshow('Potholes', potholes)

#     # Wait for a key press, and exit if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the camera capture and close all windows
# cap.release()
# cv2.destroyAllWindows()

import cv2
import numpy as np

cap = cv2.VideoCapture(
    "/Users/helenmao/Downloads/WIN_20230421_14_27_48_Pro.mp4")

pothole_threshold = 150

while cap.isOpened():
    _, img = cap.read()
    rWidth, rHeight = 288, 215
    dim = (rWidth, rHeight)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow('resized image', img)

    # First blur
    img_blur = cv2.GaussianBlur(img, (7, 7), 0)
    # kernel = np.ones((3, 3), np.uint8)
    # img_blur = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow("1st blur", img_blur)

    # Convert to graycsale
    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("grayscale", img_gray)

    # Thresholding to binary
    ret, img_thresh = cv2.threshold(img_gray, 95, 255, cv2.THRESH_BINARY)
    # img_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                            cv2.THRESH_BINARY, 11, 2)
    # cv2.imshow("thresholded", img_thresh)

    # Second blur
    img_blur2 = cv2.medianBlur(img_thresh, 15)
    # kernel = np.ones((15, 15), np.uint8)
    # img_blur2 = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow("2nd blur", img_blur2)

    # Canny Edge Detection
    img_edges = cv2.Canny(image=img_blur2, threshold1=10,
                        threshold2=100, L2gradient=True)  # Canny Edge Detection
    # cv2.imshow('Canny Edge Detection', img_edges)

    # Third blur
    # img_blur3 = cv2.medianBlur(img_edges, 15)
    kernel = np.ones((5, 5), np.uint8)
    img_blur3 = cv2.morphologyEx(img_edges, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow("3rd blur", img_blur3)

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

    cv2.drawContours(img, [c_max], 0, (0, 255, 0), 2)
    print("pothole area is the max area = %i pixels" % max(area))
    cv2.imshow('draw contour', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
