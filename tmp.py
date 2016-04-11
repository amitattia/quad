from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
from scipy import ndimage
from commandP import *

def getCenter(image):
    return ndimage.measurements.center_of_mass(image)

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)

try:
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        try
        
            myCount = 0
            
            
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
            image = frame.array
        	
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            lower_blue = np.array([100,50,50])
            upper_blue = np.array([120,255,255])
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
            loc = getCenter(mask)
            print(loc)
            print(dst[1]-loc[1])
            if(abs(dst[1]-loc[1]) > e1):
                if(dst[1] > loc[1]):
                    print('b')
                    backwards()
                else:
                    print('f')
                    forwards()
            else:
                print('fb good')
            if(abs(dst[0]-loc[0]) > e2):
                if(dst[0] > loc[0]):
                    print('l')
                    left()
                else:
                    print('r')
                    right()
            else:
                print('lf good')
            time.sleep(1)
            bus.write_block_data(address, 2, [0, 4, 0])
            time.sleep(0.2)
            bus.write_block_data(address, 2, [1, 4, 0])
            time.sleep(0.2)
            time.sleep(2)
            rawCapture.truncate(0)
        except OSError:
            print('io')
except KeyboardInterrupt:
    print('ctrl+c')
    zero()
    time.sleep(1)
    exit()
