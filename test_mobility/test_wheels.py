from pyfirmata import Arduino, util
import time
import keyboard

# Monkey patch to fix python 3.11 bug
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec


# portDir = "/dev/cu.usbmodem142101"
# dir = portDir.decode('utf8', errors='ignore')
# portDir.encode('utf-8')
# board = Arduino('/dev/cu.usbmodem142101')
board = Arduino('COM4')

# L_REN = board.get_pin('d:1:o')
# L_LEN = board.get_pin('d:2:o')
# R_REN = board.get_pin('d:7:o')
# R_LEN = board.get_pin('d:8:o')

L_RPWM = board.get_pin('d:3:p')
L_LPWM = board.get_pin('d:5:p')
R_RPWM = board.get_pin('d:9:p')
R_LPWM = board.get_pin('d:10:p')

# L_REN.write('HIGH')
# L_LEN.write('HIGH')
# R_REN.write('HIGH')
# R_LEN.write('HIGH')

while True:
    # print('stop')
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
        print('dtop')
        L_LPWM.write(0)
        L_RPWM.write(0)
        R_LPWM.write(0)
        R_RPWM.write(0)
        time.sleep(0.1)
    

    
    # print('backward')
    # L_LPWM.write(0)
    # L_RPWM.write(0.5)
    # R_LPWM.write(0)
    # R_RPWM.write(0.5)
    # time.sleep(5)
    
    # print('left')
    # L_LPWM.write(0)
    # L_RPWM.write(0.5)
    # R_LPWM.write(0.5)
    # R_RPWM.write(0)
    # time.sleep(5)
    
    # print('right')
    # L_LPWM.write(0.5)
    # L_RPWM.write(0)
    # R_LPWM.write(0)
    # R_RPWM.write(0.5)
    # time.sleep(5)
    
    # print('stop')
    # L_LPWM.write(0)
    # L_RPWM.write(0)
    # R_LPWM.write(0)
    # R_RPWM.write(0)
    # time.sleep(5)


