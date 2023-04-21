from pymata4 import pymata4
import time
import sys

# Monkey patch to fix python 3.11 bug
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
    
file_path = inspect.getfile()
print(file_path)


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


board = pymata4.Pymata4()
try:
    sonar(board, TRIG, ECHO, the_callback)
    board.shutdown()
except (KeyboardInterrupt, RuntimeError):
    board.shutdown()
    sys.exit(0)
