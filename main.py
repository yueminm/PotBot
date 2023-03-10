# main python file
# import all libraries
import cv2
# python arduino integration package
import pyfirmata
import time

def main():
    # FLAGS
    POTHOLE_FOUND = False
    POTHOLE_REACHED = False
    POTHOLE_FILLED = False

    # CONSTANTS
    # unit: cm
    CAR_LENGTH = 0
    CAR_WIDTH = 0
    ROLLER_LENGTH = 0
    CAM_HEIGHT = 0
    CAM_ANGLE = 0
    # unit: cm^3 / s
    ASP_FLOW_RATE = 0
    # unit: cm/s
    WHEEL_DRIVING_SPEED = 0
    WHEEL_TURNING_SPEED = 0

    while not POTHOLE_FILLED:
        if not POTHOLE_REACHED:
            if not POTHOLE_FOUND:
                #keep driving forward until a pothole is in view
                POTHOLE_FOUND = True

            distance, angle = findPothole()
            # drive towards the pothole until it is reached
        else:
            # Auger turn for some seconds and stop
            # drive half of a body length
            # turn on water sprayer
            # drive half of a body length + roller length
            # Stop for a second
            # drive backwards a full roller Length
            # drive forwards a full roller length
            # stop water sprayer
            POTHOLE_FILLED = True

    return True

def findPothole():
    # define a video capture object
    vid = cv2.VideoCapture(0)
    while(True):
        
        # Capture the video frame
        # by frame
        ret, frame = vid.read()

        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    potholeLocation = (0, 0)
    potholeSize = 100
    return distance, angle


# ToDo calculate volume of pothole
def calcVolume(video, center, depth):
    area = 0
    volume = area * depth
    return volume

main()