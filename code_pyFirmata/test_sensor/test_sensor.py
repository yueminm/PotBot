from pyfirmata import ArduinoMega, util
import time

# Monkey patch to fix python 3.11 bug
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
    


board = ArduinoMega('COM5')

trig = board.get_pin('d:52:o')
echo = board.get_pin('d:51:i')

while True:
    duration = echo.ping()

    if duration:
            # Normal distance (speed of sound based)
            distance = util.ping_time_to_distance(duration)

            # Distance based on calibration points.
            calibration = [(680.0, 10.0), (1460.0, 20.0), (2210.0, 30.0)]
            cal_distance = util.ping_time_to_distance(duration, calibration)

            print ("Distance: \t%scm \t%scm (calibrated) \t(%ss)" \
    % (distance, cal_distance, duration))
    else:
        print ("No distance!")

    time.sleep(0.2)
