from Arduino import Arduino
import time

board = Arduino() # plugged in via USB, serial com at rate 115200

front_left_1 = 2
front_left_2 = 3
rear_left_1 = 4
rear_left_2 = 5
front_right_1 = 6
front_right_2 = 7
rear_right_1 = 8
rear_right_2 = 9

board.pinMode(front_left_1, "OUTPUT")
board.pinMode(front_left_2, "OUTPUT")
board.pinMode(rear_left_1, "OUTPUT")
board.pinMode(rear_left_2, "OUTPUT")
board.pinMode(front_right_1, "OUTPUT")
board.pinMode(front_right_2, "OUTPUT")
board.pinMode(rear_right_1, "OUTPUT")
board.pinMode(rear_right_2, "OUTPUT")



while True:
    board.digitalWrite(front_left_1, "HIGH")
    board.digitalWrite(front_left_2, "LOW")
    board.digitalWrite(rear_left_1, "HIGH")
    board.digitalWrite(rear_left_2, "LOW")
    board.digitalWrite(front_right_1, "HIGH")
    board.digitalWrite(front_right_2, "LOW")
    board.digitalWrite(rear_right_1, "HIGH")
    board.digitalWrite(rear_right_2, "LOW")

    time.sleep(5)

    board.digitalWrite(front_left_1, "HIGH")
    board.digitalWrite(front_left_2, "LOW")
    board.digitalWrite(rear_left_1, "HIGH")
    board.digitalWrite(rear_left_2, "LOW")
    board.digitalWrite(front_right_1, "HIGH")
    board.digitalWrite(front_right_2, "LOW")
    board.digitalWrite(rear_right_1, "HIGH")
    board.digitalWrite(rear_right_2, "LOW")

    time.sleep(5)