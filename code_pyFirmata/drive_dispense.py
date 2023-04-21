from pyfirmata import ArduinoMega, util
import time
import keyboard

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
    
    FillingFlag = 0
    
    if keyboard.is_pressed('w'):
        print('forward')
        L_LPWM.write(0.5)
        L_RPWM.write(0)
        R_LPWM.write(0.5)
        R_RPWM.write(0)
        time.sleep(sleepTime)

    if keyboard.is_pressed('s'):
        print('backward')
        L_LPWM.write(0)
        L_RPWM.write(0.5)
        R_LPWM.write(0)
        R_RPWM.write(0.5)
        time.sleep(sleepTime)

    if keyboard.is_pressed('a'):
        print('left')
        L_LPWM.write(0.5)
        L_RPWM.write(0)
        R_LPWM.write(0)
        R_RPWM.write(0.5)
        time.sleep(sleepTime)

    if keyboard.is_pressed('d'):
        print('right')
        L_LPWM.write(0)
        L_RPWM.write(0.5)
        R_LPWM.write(0.5)
        R_RPWM.write(0)
        time.sleep(sleepTime)

    if keyboard.is_pressed('q'):
        print('stop')
        L_LPWM.write(0)
        L_RPWM.write(0)
        R_LPWM.write(0)
        R_RPWM.write(0)
        time.sleep(sleepTime)
    
    if keyboard.is_pressed('p'):
        FillingFlag = 1
        print('auger turning')
        # A_LPWM.write(0)
        # A_RPWM.write(0.5)
        # time.sleep(sleepTime)
        
    if FillingFlag == 1:
        A_LPWM.write(0)
        A_RPWM.write(0.5)
        time.sleep(5)
    
    if keyboard.is_pressed('l'):
        print("pump")
        pump.write(1)
        time.sleep(sleepTime)

