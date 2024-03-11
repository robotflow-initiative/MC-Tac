import os, sys
import cv2
import numpy as np
import base64

cam_id = int(sys.argv[0])
cam = cv2.VideoCapture(cam_id)

if not cam.isOpened():
    print(f"Unable to open camera with device id {cam_id}")
    exit()

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200)

while True:
    rval, frame = cam.read()
    if rval:
        cv2.imshow('Camera', frame)
    
    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()