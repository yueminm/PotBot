from pyfirmata import Arduino, util
import time
import keyboard

# Monkey patch to fix python 3.11 bug
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec


board = Arduino('COM4')

L_RPWM = board.get_pin('d:3:p')
L_LPWM = board.get_pin('d:5:p')
R_RPWM = board.get_pin('d:9:p')
R_LPWM = board.get_pin('d:10:p')

while True:
    L_LPWM.write(0)
    L_RPWM.write(0)
    R_LPWM.write(0)
    R_RPWM.write(0)
    
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


