from pyfirmata import Arduino, util
import time
import keyboard

# Monkey patch to fix python 3.11 bug
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec


board1 = Arduino('COM4')

L_RPWM = board1.get_pin('d:3:p')
L_LPWM = board1.get_pin('d:5:p')
R_RPWM = board1.get_pin('d:9:p')
R_LPWM = board1.get_pin('d:10:p')


board2 = Arduino('COM3')

A_RPWM = board2.get_pin('d:3:p')
A_LPWM = board2.get_pin('d:5:p')
A_RENABLE = board2.get_pin('d:4:o')
A_LENABLE = board2.get_pin('d:2:o')

while True:
    L_LPWM.write(0)
    L_RPWM.write(0)
    R_LPWM.write(0)
    R_RPWM.write(0)
    
    A_RPWM.write(0) 
    A_LPWM.write(0)
    A_RENABLE.write(1)
    A_LENABLE.write(1)
    
    if keyboard.is_pressed('w'):
        print('forward')
        L_LPWM.write(0.5)
        L_RPWM.write(0)
        R_LPWM.write(0.5)
        R_RPWM.write(0)
        time.sleep(0.1)

    if keyboard.is_pressed('s'):
        print('backward')
        L_LPWM.write(0)
        L_RPWM.write(0.5)
        R_LPWM.write(0)
        R_RPWM.write(0.5)
        time.sleep(0.1)

    if keyboard.is_pressed('a'):
        print('left')
        L_LPWM.write(0)
        L_RPWM.write(0.5)
        R_LPWM.write(0.5)
        R_RPWM.write(0)
        time.sleep(0.1)

    if keyboard.is_pressed('d'):
        print('right')
        L_LPWM.write(0.5)
        L_RPWM.write(0)
        R_LPWM.write(0)
        R_RPWM.write(0.5)
        time.sleep(0.1)

    if keyboard.is_pressed('q'):
        print('stop')
        L_LPWM.write(0)
        L_RPWM.write(0)
        R_LPWM.write(0)
        R_RPWM.write(0)
        time.sleep(0.1)
    
    if keyboard.is_pressed('o'):
        print('auger forward')
        A_LPWM.write(0.5)
        A_RPWM.write(0)
        time.sleep(0.1)
    
    if keyboard.is_pressed('p'):
        print('auger backward')
        A_LPWM.write(0)
        A_RPWM.write(0.5)
        time.sleep(0.1)
