from pyfirmata import ArduinoMega, util
import time
import keyboard
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
from pothole_detection_hist_video import getThresh, imageInfo
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

#initialize board
board = ArduinoMega('COM4')
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

#initialize the camera
vid = cv2.VideoCapture(0)

#initialize the angle array and the time between the two (for velocity calcs)
angleMem = []
times = []
forwardConstant = 0.5
maxModifier = 0.5
kp = 1
kd = 0.25


#gets the velocity of the pothole in the images
def getVelocity(positions,times):
    if len(positions) < 5:
        return 0
    else:
        velocity=0
        for i in range(4):
            velocity = velocity + (positions[i]- positions[i+1]) / (times[i] -times[i+1])
    return int(velocity/4)

while True:
    L_LPWM.write(0)
    L_RPWM.write(0)
    R_LPWM.write(0)
    R_RPWM.write(0)
    
    _, frame = vid.read()
    thresh = getThresh(frame)
    _, angleErr, xValue, yValue = imageInfo(frame,thresh)

    angleMem.append(angleErr)
    times.append(time.time())
    if len(angleMem) == 5:
        velAngleErr = getVelocity(angleMem,times)
        angleMem.pop(0)
        times.pop(0)

    #ensure the modifier is not too great
    modifier = kp*angleErr + kd*velAngleErr
    if abs(modifier) > maxModifier:
        modifier = maxModifier/modifier  * abs(modifier)

    L_RPWM.write(forwardConstant+modifier)
    R_RPWM.write(forwardConstant+modifier)

    time.sleep(sleepTime)
   