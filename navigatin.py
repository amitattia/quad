from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
from scipy import ndimage
import smbus
bus = smbus.SMBus(1)
address = 0x04

def getCenter(image):
    return ndimage.measurements.center_of_mass(image)
    
def zero():
    bus.write_block_data(address, 2, [0, 4, 0])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [1, 4, 0])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [2, 4, 0])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [3, 4, 0])
    time.sleep(0.2)

def up():
    bus.write_block_data(address, 2, [2, 4, 200])
    time.sleep(0.2)

def down():
    bus.write_block_data(address, 2, [2, 3, 50])
    time.sleep(0.2)

def forwards():
    bus.write_block_data(address, 2, [1, 4, 200])
    time.sleep(0.2)

def backwards():
    bus.write_block_data(address, 2, [1, 3, 50])
    time.sleep(0.2)

def right():
    bus.write_block_data(address, 2, [0, 4, 100])
    time.sleep(0.2)

def left():
    bus.write_block_data(address, 2, [0, 3, 50])
    time.sleep(0.2)    

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
e1 = 0.00000
e2 = 0.00000
 
# allow the camera to warmup
time.sleep(0.1)

dst = (320, 240)

try:
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        try:
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
                    print('f')
                    forwards()
                else:
                    print('b')
                    backwards()
            #if(abs(dst[0]-loc[0]) > e2):
            #    if(dst[0] > loc[0]):
            #        print('l')
            #        left()
            #    else:
            #        print('r')
            #        right()
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
