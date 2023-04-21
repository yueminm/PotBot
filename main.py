from pyfirmata import ArduinoMega, util
import time
import keyboard

# Monkey patch to fix python 3.11 bug
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

board = ArduinoMega('COM5')

# Wheels
L_LEN = board.get_pin('d:50:o')
L_REN = board.get_pin('d:49:o')
L_RPWM = board.get_pin('d:9:p')
L_LPWM = board.get_pin('d:3:p')
R_RPWM = board.get_pin('d:10:p')
R_LPWM = board.get_pin('d:5:p')

# Auger
A_RENABLE = board.get_pin('d:48:o')
A_LENABLE = board.get_pin('d:47:o')
A_RPWM = board.get_pin('d:11:p')
A_LPWM = board.get_pin('d:6:p')

# Pump
PUMP = board.get_pin('d:46:o')

# Initialization
L_LEN.write(1)
L_REN.write(1)
A_RENABLE.write(1)
A_LENABLE.write(1)
PUMP.write(0)

"""
print('forward')
L_LPWM.write(0.5)
L_RPWM.write(0)
R_LPWM.write(0.5)
R_RPWM.write(0)

print('backward')
L_LPWM.write(0)
L_RPWM.write(0.5)
R_LPWM.write(0)
R_RPWM.write(0.5)

print('left')
L_LPWM.write(0.5)
L_RPWM.write(0)
R_LPWM.write(0)
R_RPWM.write(0.5)

print('right')
L_LPWM.write(0)
L_RPWM.write(0.5)
R_LPWM.write(0.5)
R_RPWM.write(0)

print('auger turning')
A_LPWM.write(0)
A_RPWM.write(0.5)

print("pump")
PUMP.write(1)
"""

sleepTime = 0.1
thresh_low = 0
thresh_high = 0

NavigationFlag = 1
FillingFlag = 0
FlatteningFlag = 0
MoveAwayFlag = 0
OperationFinished = 0

FillingTime = 4
FlatteningTime = 5
MoveAwayTime = 5


while True:
    L_LPWM.write(0)
    L_RPWM.write(0)
    R_LPWM.write(0)
    R_RPWM.write(0)

    A_RPWM.write(0)
    A_LPWM.write(0)
    
    PUMP.write(0)

    if NavigationFlag == 1:
    # Place holder: CV output x, y
    
        if (x > thresh_low and x < thresh_high):
            # Go forward
            L_LPWM.write(0.5)
            L_RPWM.write(0)
            R_LPWM.write(0.5)
            R_RPWM.write(0)
        
        if (x < thresh_low):
            # Trun left
            L_LPWM.write(0.5)
            L_RPWM.write(0)
            R_LPWM.write(0)
            R_RPWM.write(0.5)
        
        if (x > thresh_low):
            # Turn right
            L_LPWM.write(0)
            L_RPWM.write(0.5)
            R_LPWM.write(0.5)
            R_RPWM.write(0)
            
        if ():
            NavigationFlag = 0
            FillingFlag = 1
        
        continue
    
    if FillingFlag == 1:
        A_LPWM.write(0)
        A_RPWM.write(0.5)
        FillingFlag = 0
        time.sleep(5)
    
    if FlatteningFlag == 1:
        PUMP.write(1)
        L_LPWM.write(0.5)
        L_RPWM.write(0)
        R_LPWM.write(0.5)
        R_RPWM.write(0)
        FlatteingFlag = 2
        time.sleep(FlatteningTime)
    
    if FlatteningFlag == 2:
        PUMP.write(1)
        L_LPWM.write(0)
        L_RPWM.write(0.5)
        R_LPWM.write(0)
        R_RPWM.write(0.5)
        FlatteningFlag = 0
        MoveAwayFlag = 1
        time.sleep(FlatteningTime)
    
    if MoveAwayFlag == 1:
        L_LPWM.write(0.5)
        L_RPWM.write(0)
        R_LPWM.write(0.5)
        R_RPWM.write(0)
        OperationFinished = 1
        MoveAwayFlag = 0
        time.sleep(MoveAwayTime)
    
    if OperationFinished == 1:
        break
    
    
