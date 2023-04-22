import cv2
import numpy as np
  
# # Let's load a simple image with 3 black squares
# image = cv2.imread('images/test_1.jpg')
  
# # Grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
# # Find Canny edges
# edged = cv2.Canny(gray, 100, 200)
  
# # Finding Contours
# # Use a copy of the image e.g. edged.copy()
# # since findContours alters the image
# contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  
# cv2.imshow('Canny Edges After Contouring', edged)
  
# print("Number of Contours found = " + str(len(contours)))
  
# # Draw all contours
# # -1 signifies drawing all contours
# cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# c = max(contours, key = cv2.contourArea)
# x,y,w,h = cv2.boundingRect(c)
# cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
  
# cv2.imshow('Contours', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np

# Load the image
image = cv2.imread('images/test_1.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold, _ = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Apply edge detection
edges = cv2.Canny(gray, threshold*0.3, threshold)
cv2.imshow('Edges', edges)

# Close the edges
kernel = np.ones((10, 10), np.uint8)
closed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closed Edges', closed_edges)

# Find the contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# Compute the areas of the contours
areas = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    areas.append(area)

# Compute the area inside the edges
total_area = image.shape[0] * image.shape[1]
area_inside_edges = total_area - sum(areas)

# Print the area inside the edges
print('Area inside edges:', area_inside_edges)
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()