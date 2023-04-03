from pyfirmata import Arduino, util
import time
import keyboard

# Monkey patch to fix python 3.11 bug
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
    
board = Arduino('COM4')

A_RPWM = board.get_pin('d:3:p')
A_LPWM = board.get_pin('d:5:p')
A_RENABLE = board.get_pin('d:4:o')
A_LENABLE = board.get_pin('d:2:o')
# P_RPWM = board.get_pin('d:9:p')
# P_LPWM = board.get_pin('d:10:p')

while True:  
    A_RPWM.write(0) 
    A_LPWM.write(0)
    A_RENABLE.write(1)
    A_LENABLE.write(1)
    
    # P_RPWM.write(0)
    # P_LPWM.write(0)
    
    if keyboard.is_pressed('w'):
        print('auger forward')
        A_LPWM.write(0.5)
        A_RPWM.write(0)
        time.sleep(0.1)
    
    if keyboard.is_pressed('s'):
        print('auger backward')
        A_LPWM.write(0)
        A_RPWM.write(0.5)
        time.sleep(0.1)
        
    # if keyboard.is_pressed('p'):
    #     print('pump on')
    #     P_LPWM.write(0.5)
    #     P_RPWM.write(0)
    #     time.sleep(0.1)