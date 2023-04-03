import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

# test images
img = cv2.imread( "/Users/jaimearomero/Desktop/Tello-master/jacket.jpg")
img2 = cv2.imread( "/Users/jaimearomero/Desktop/Tello-master/grainyJacket.jpg")
img3 = cv2.imread( "/Users/jaimearomero/Desktop/Tello-master/2.png")
img4 = cv2.imread( "/Users/jaimearomero/Desktop/Tello-master/3.png")

img5 = cv2.imread( "/Users/jaimearomero/Desktop/Coding on a plane/IMG_4258.jpg")
img6 = cv2.imread( "/Users/jaimearomero/Desktop/Coding on a plane/IMG_4261.jpg")
img7 = cv2.imread( "/Users/jaimearomero/Desktop/Coding on a plane/IMG_4257.jpg")
img8 = cv2.imread( "/Users/jaimearomero/Desktop/Coding on a plane/IMG_4262.jpg")

# takes an image and returns the best center of threshold values (both high and low)
def getThresh(img):

    hues = [0]*180 # will store the histogram (Hue values in python only have 180 degrees)
    width, height = img.shape[1], img.shape[0]


    # resize the image into something managable
    rWidth, rHeight = 288,215
    dim = (rWidth,rHeight)
    img = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #This places everything into the histogram 
    for row in range(rWidth):
        for col in range(rHeight):
            hues[img[col][row][0]] = hues[img[col][row][0]] + 1


    idx = 150 # target hue
    max = 0
    maxValue = 0

    #finds the peak around the Target hue 
    for i in range(30):
        index = idx + i 
        if index > 179:
            index = index - 180
        if hues[index] > maxValue:
            max = index
            maxValue = hues[index]
    thresh = (max - 5,max+5)
            
    # plots the histogram
    # print(thresh)
    # plt.plot(range(180),hues)
    # plt.show()

    #shows the resized image
    # img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    # cv2.imshow('image',img)
    # cv2.waitKey(1) & 0xFF == ord('q')
    # print(thresh)
    return thresh
            
    
# returns the size dif (this was for another project) & the dir is the pixle
# difference between center and the center of the pink ring  
def imageInfo(img,thresh):
    # print(type(img))
    if img is None:
        return 100,0
    width, height = img.shape[1], img.shape[0]

    #resize the image into something managable
    rWidth, rHeight = 288,215
    dim = (rWidth,rHeight)
    img = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #threshold for the colors
    if thresh[1] > 179:
        binary_img1 = cv2.inRange(img, (thresh[0], 0, 0), (180, 255, 255))
        binary_img2 = cv2.inRange(img, (0, 0, 0), (thresh[1], 255, 255))
        binary_img = binary_img1 & binary_img2
    else:
        binary_img = cv2.inRange(img, (thresh[0], 0, 0), (thresh[1], 255, 255))

    blur = cv2.GaussianBlur(binary_img,(5,5),0)
    ret3,binary_img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    #find all target pixles and their placement within the image
    size = 0
    countX = 0
    countY = 0
    for row in range(rWidth):
        for col in range(rHeight):
            if binary_img[col][row]:
                size  = size + 1
                countX = countX + row
                countY = countY + col
           
    if countX == 0:
        return 100,0
    
    contourXCenter = int(countX/size)
    contourYCenter = int(countY/size)

    # print the image
    cv2.circle(binary_img,(contourXCenter,contourYCenter),20,(255,0,0),3)
    cv2.imshow('image',binary_img)
    cv2.waitKey(1) & 0xFF == ord('q')

    sizeErr = math.sqrt(12372/size) # FIND THE DIFFERENCE BETWEEN THE AREAS
    distFromCenter = rWidth/2 - contourXCenter
    dir = int(math.degrees(math.atan2(((4/3)*(distFromCenter)),rWidth)))
    return sizeErr, dir

thresh = getThresh(img8)
imageInfo(img8,thresh)