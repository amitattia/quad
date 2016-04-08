from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
from scipy import ndimage
from commandP import *

def scanArea(threshold = 400):
    myCount = 0
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))
    time.sleep(0.2)
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        if myCount%4 == 0:
            print('f')
            forwards()
        if myCount%4 == 1:
            print('r')
            right()
        if myCount%4 == 2:
            print('b')
            backwards()
        if myCount%4 == 3:
            print('l')
            left()
        time.sleep(2)
        myCount = myCount + 1
        image = frame.array
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([100,50,50])
        upper_blue = np.array([120,255,255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        if cv2.countNonZero(mask) > threshold:
            print(cv2.countNonZero(mask))
            return True
        if myCount > 6:
            return False
            
if __name__ == "__main__":
    scanArea()
