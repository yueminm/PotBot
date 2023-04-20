from pyfirmata import ArduinoMega, util
import time

# Monkey patch to fix python 3.11 bug
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
    


board = ArduinoMega('COM5')

trigpin = board.get_pin('d:52:o')
echopin = board.get_pin('d:51:o')

while True:
    trigpin.write(0)
    board.pass_time(0.5)
    trigpin.write(1)
    board.pass_time(0.00001)
    trigpin.write(0)
    limit_start = time.time()
    
    while echopin.read() != 1:
        if time.time() - limit_start > 1:
            break
        pass
    
    start = time.time()
    
    while echopin.read() != 0:
        pass
    
    stop = time.time()
    
    time_elapsed = stop - start
    print((time_elapsed) * 34300 / 2)
    board.pass_time(1)
    
    