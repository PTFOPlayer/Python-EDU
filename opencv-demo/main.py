#program detecting blue color in camera image

import cv2
import numpy as np

cv2.namedWindow("image")
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('image',frame)
    
    #display color mask
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #detect color (blue)
    lower_band = np.array([80,80,200])
    upper_band = np.array([130,255,255])
    mask = cv2.inRange(frame, lower_band, upper_band)
    result = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('mask', result)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    

