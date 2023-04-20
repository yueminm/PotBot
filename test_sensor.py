from pyfirmata import ArduinoMega, util
import time

# Monkey patch to fix python 3.11 bug
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
    


board = ArduinoMega('COM5')

trig = board.get_pin('d:51:o')
echo = board.get_pin('d:52:i')

it = util.Iterator(board)
it.start()

trig.write(0)
time.sleep(2)
start = 0
end = 0

while True:
    # trig.write(0)
    # # time.sleep(0.5)
    # board.pass_time(0.5)
    # trig.write(1)   
    # # time.sleep(0.00001)
    # board.pass_time(0.00001)
    # trig.write(0)
    
    # # print(echo.read())
    # while echo.read() == False:
    #     pass
    # start = time.time()
    #     # break

    # # start = time.time()

    # while echo.read() == True:
    #     pass
    # end = time.time()
    #     # break
    #     # print(2)

    
    # TimeElapsed = end - start
    # # print("start:  ", start, "  end:  ", "  Elapse: ",TimeElapsed)
    # distance = (TimeElapsed * 343) / 2

    # print("Measured Distance = {} cm".format(distance))
    
    trig.write(True)
    time.sleep(0.00001)
    trig.write(False)

    # Read the distance
    duration = echo.read_duration()
    distance = duration / 58.2

    print('Distance:', distance, 'cm')
    time.sleep(1)