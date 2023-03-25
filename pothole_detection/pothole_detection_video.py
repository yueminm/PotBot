# importing required libraries
import cv2
import numpy as np
  
# taking the input from webcam
vid = cv2.VideoCapture(0)
  
while True:
    
    detected = False
    # capturing the current frame
    _, frame = vid.read()
    
    # cv2.imshow('openCV', frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
    
    height = len(frame)
    width = len(frame[0])
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_purple = np.array([130, 0, 220], dtype='uint8')
    upper_purple = np.array([170, 255, 255], dtype='uint8')

    mask = cv2.inRange(frame_hsv, lower_purple, upper_purple)
    if not any(255 in x for x in mask):
        detected = False
        print('No potholes in the view')
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    else:
        detected = True
        print('Pothole detected')
        edges = np.where(mask==255)
        closest_point = np.where(edges[0]==edges[0].max())
        i_closest = closest_point[0][0]
        [row, col] = [edges[0][i_closest], edges[1][i_closest]]
        print(row, col)
        frame_processed = cv2.circle(frame, (col, row), 10, (0, 255, 0), 5)
        cv2.imshow('Video', frame_processed)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
vid.release()
cv2.destroyAllWindows()