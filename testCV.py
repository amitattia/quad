import time
import io
import picamera
import picamera.array
import cv2
import smbus
import numpy as np
from scipy import ndimage
bus = smbus.SMBus(1)
address = 0x04

def getCenter(image):
	return ndimage.measurements.center_of_mass(image)

def all():
    bus.write_block_data(address, 2, [0, 1, 107])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [1, 1, 107])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [2, 1, 107])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [3, 6, 148])
    time.sleep(0.2)

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

stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    time.sleep(2)
    dst = (1024/2, 768/2)
    e1 = 0
    e2 = 0
    while True:
        try:
            time.sleep(2)
                
            camera.capture(stream, format='jpeg')
            # Construct a numpy array from the stream
            data = np.fromstring(stream.getvalue(), dtype=np.uint8)
            # Decode" the image from the array, preserving colour
            frame = cv2.imdecode(data, 1)
            # OpenCV returns an array with data in BGR order. If you want RGB instead
            # use the following...
            frame = frame[:, :, ::-1]
            
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_blue = np.array([100,50,50])
            upper_blue = np.array([120,255,255])
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
            cv2.imshow('mask', mask)
            loc = getCenter(mask)
            print('loc')
            print(loc)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print('fb')
            print(dst[0]-loc[0])
            if(abs(dst[0]-loc[0]) > e1):
                if(dst[0] > loc[0]):
                    print('f')
                else:
                    print('b')
            time.sleep(2)