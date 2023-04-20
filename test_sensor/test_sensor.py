from pyfirmata import ArduinoMega, util
import time

# Monkey patch to fix python 3.11 bug
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
    


board = ArduinoMega('COM5')

trig = board.get_pin('d:52:o')
echo = board.get_pin('d:51:i')

it = util.Iterator(board)
it.start()

trig.write(0)
time.sleep(2)

while True:
    time.sleep(0.5)

    trig.write(1)   
    time.sleep(0.00001)
    trig.write(0)
    
    # print(echo.read())
    while echo.read() == False:
        start = time.time()

    while echo.read() == True:
        end = time.time()
    
    TimeElapsed = end - start
    distance = (TimeElapsed * 34300) / 2

    print("Measured Distance = {} cm".format(distance))