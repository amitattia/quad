from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
from scipy import ndimage
from commandP import *

def getCenter(image):
    return ndimage.measurements.center_of_mass(image)

def navigateImg():
    moveTime = 0.5
    sleepTime = 2
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))
    e1 = 20.00000
    e2 = 20.00000
    time.sleep(0.1)
    dst = (320, 240)
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        try:
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
            image = frame.array
            w = 0
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            lower_blue = np.array([100,50,50])
            upper_blue = np.array([120,255,255])
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
            loc = getCenter(mask)
            print(dst[1]-loc[1])
            print(dst[0]-loc[0])
            if(abs(dst[1]-loc[1]) > e1):
                if(dst[1] > loc[1]):
                    print('b')
                    backwards(20+int((dst[1]-loc[1])/3))
                else:
                    print('f')
                    forwards(20-int((dst[1]-loc[1])/3))
            else:
                print('fb good')
                w = w + 1
            if(abs(dst[0]-loc[0]) > e2):
                if(dst[0] > loc[0]):
                    print('l')
                    left(20+int((dst[0]-loc[0])/3))
                else:
                    print('r')
                    right(20-int((dst[0]-loc[0])/3))
            else:
                print('lf good')
                w = w + 1
            if w == 2:
                print('drop')
            time.sleep(moveTime)
            zero()
            time.sleep(sleepTime)
            rawCapture.truncate(0)
        except OSError:
            print('io')

if __name__ == "__main__":
    navigateImg()
