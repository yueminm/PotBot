from pyfirmata import ArduinoMega, util
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
    

board = ArduinoMega('COM5')

L_LEN = board.get_pin('d:50:o')
L_REN = board.get_pin('d:49:o')
L_RPWM = board.get_pin('d:9:p')
L_LPWM = board.get_pin('d:3:p')

R_RPWM = board.get_pin('d:10:p')
R_LPWM = board.get_pin('d:5:p')

A_RENABLE = board.get_pin('d:48:o')
A_LENABLE = board.get_pin('d:47:o')
A_RPWM = board.get_pin('d:11:p')
A_LPWM = board.get_pin('d:6:p')

pump = board.get_pin('d:46:o')

sleepTime = 0.1

while True:
    L_LEN.write(1)
    L_REN.write(1)
    L_LPWM.write(0)
    L_RPWM.write(0)

    R_LPWM.write(0)
    R_RPWM.write(0)
    
    A_RENABLE.write(1)
    A_LENABLE.write(1)
    A_RPWM.write(0) 
    A_LPWM.write(0)

    pump.write(0)
    
    _, frame = vid.read()
    thresh = getThresh(frame)
    _, angleErr, xValue, yValue = imageInfo(frame,thresh)
    