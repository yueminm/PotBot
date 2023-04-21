from pymata4 import pymata4
import time
import keyboard
import sys

# Monkey patch to fix python 3.11 bug
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec



# board = pymata4.Pymata4() 
# board.shutdown()
board = pymata4.Pymata4()

# Wheels
L_LEN = 50
L_REN = 49
L_RPWM = 9
L_LPWM = 3
R_RPWM = 10
R_LPWM = 5
board.set_pin_mode_digital_output(L_LEN)
board.set_pin_mode_digital_output(L_REN)
board.set_pin_mode_pwm_output(L_RPWM)
board.set_pin_mode_pwm_output(L_LPWM)
board.set_pin_mode_pwm_output(R_RPWM)
board.set_pin_mode_pwm_output(R_LPWM)

# Auger
A_RENABLE = 48
A_LENABLE = 47
A_RPWM = 11
A_LPWM = 6
board.set_pin_mode_digital_output(A_RENABLE)
board.set_pin_mode_digital_output(A_LENABLE)
board.set_pin_mode_pwm_output(A_RPWM)
board.set_pin_mode_pwm_output(A_LPWM)

# Pump
PUMP = 46
board.set_pin_mode_digital_output(PUMP)

# UR sensor
TRIG = 51
ECHO = 52
DISTANCE_CM = 2


def the_callback(data):
    print(f'Distance in cm: {data[DISTANCE_CM]}')


def sonar(my_board, trigger_pin, echo_pin, callback):
    my_board.set_pin_mode_sonar(trigger_pin, echo_pin, callback)
    while True:
        try:
            time.sleep(.01)
            print(f'data read: {my_board.sonar_read(TRIG)}')
        except KeyboardInterrupt:
            my_board.shutdown()
            sys.exit(0)

sleepTime = 0.1

# L_LEN = board.get_pin('d:50:o')
# L_REN = board.get_pin('d:49:o')
# L_RPWM = board.get_pin('d:9:p')
# L_LPWM = board.get_pin('d:3:p')

# R_RPWM = board.get_pin('d:10:p')
# R_LPWM = board.get_pin('d:5:p')

# A_RENABLE = board.get_pin('d:48:o')
# A_LENABLE = board.get_pin('d:47:o')
# A_RPWM = board.get_pin('d:11:p')
# A_LPWM = board.get_pin('d:6:p')

# pump = board.get_pin('d:46:o')


speed = 100
board.digital_write(L_LEN, 1)
board.digital_write(L_REN, 1)

board.digital_write(A_RENABLE, 1)
board.digital_write(A_LENABLE, 1)

while True:
    # UR senor
    sonar(board, TRIG, ECHO, the_callback)
    
    # Wheels
    # board.digital_write(L_LEN, 1)
    # board.digital_write(L_REN, 1)
    board.pwm_write(L_LPWM, 0)
    board.pwm_write(L_RPWM, 0)
    board.pwm_write(R_LPWM, 0)
    board.pwm_write(R_RPWM, 0)
    
    # Auger
    # board.digital_write(A_RENABLE, 1)
    # board.digital_write(A_LENABLE, 1)
    board.pwm_write(A_LPWM, 0)
    board.pwm_write(A_RPWM, 0)

    # Pump
    board.digital_write(PUMP, 0)
    
    if keyboard.is_pressed('w'):
        print('forward')
        board.pwm_write(L_LPWM, speed)
        board.pwm_write(L_RPWM, 0)
        board.pwm_write(R_LPWM, speed)
        board.pwm_write(R_RPWM, 0)

        time.sleep(sleepTime)

    if keyboard.is_pressed('s'):
        print('backward')
        board.pwm_write(L_LPWM, 0)
        board.pwm_write(L_RPWM, speed)
        board.pwm_write(R_LPWM, 0)
        board.pwm_write(R_RPWM, speed)

        time.sleep(sleepTime)

    if keyboard.is_pressed('a'):
        print('left')
        board.pwm_write(L_LPWM, speed)
        board.pwm_write(L_RPWM, 0)
        board.pwm_write(R_LPWM, 0)
        board.pwm_write(R_RPWM, speed)

        time.sleep(sleepTime)

    if keyboard.is_pressed('d'):
        print('right')
        board.pwm_write(L_LPWM, 0)
        board.pwm_write(L_RPWM, speed)
        board.pwm_write(R_LPWM, speed)
        board.pwm_write(R_RPWM, 0)

        time.sleep(sleepTime)

    if keyboard.is_pressed('q'):
        print('stop')
        board.pwm_write(L_LPWM, 0)
        board.pwm_write(L_RPWM, 0)
        board.pwm_write(R_LPWM, 0)
        board.pwm_write(R_RPWM, 0)

        time.sleep(sleepTime)
    
    if keyboard.is_pressed('p'):
        print('auger turning')
        board.pwm_write(A_LPWM, 0)
        board.pwm_write(A_RPWM, speed)

        time.sleep(sleepTime)
    
    if keyboard.is_pressed('l'):
        print("pump")
        board.digital_write(PUMP, 1)
        time.sleep(sleepTime)

    if keyboard.is_pressed('m'):
        board.shutdown()

