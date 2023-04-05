from pyfirmata import Arduino, util
import time
import keyboard
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
from pothole_detection_hist_video import getThresh, imageInfo

# Monkey patch to fix python 3.11 bug
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec


board = Arduino('COM4')

L_RPWM = board.get_pin('d:3:p')
L_LPWM = board.get_pin('d:5:p')
R_RPWM = board.get_pin('d:9:p')
R_LPWM = board.get_pin('d:10:p')

vid = cv2.VideoCapture(0)

while True:
    L_LPWM.write(0)
    L_RPWM.write(0)
    R_LPWM.write(0)
    R_RPWM.write(0)
    
    _, frame = vid.read()
    thresh = getThresh(frame)
    _, _, xValue, yValue = imageInfo(frame,thresh)
    if yValue <= 680 and yValue >= 600:
        print('forward')
        L_LPWM.write(0.5)
        L_RPWM.write(0)
        R_LPWM.write(0.5)
        R_RPWM.write(0)
        time.sleep(0.1)
    
    if yValue < 600:
        print('left')
        L_LPWM.write(0)
        L_RPWM.write(0.5)
        R_LPWM.write(0.5)
        R_RPWM.write(0)
        time.sleep(0.1)
    
    if yValue > 680:
        print('right')
        L_LPWM.write(0.5)
        L_RPWM.write(0)
        R_LPWM.write(0)
        R_RPWM.write(0.5)
        time.sleep(0.1)