import time
import microstacknode.hardware.gps.l80gps
from commandP import *

def getCor(data):
    cor = (data['latitude'], data['longitude'])
    return cor

def gpsNavigation():
    gps = microstacknode.hardware.gps.l80gps.L80GPS()
    e1 = 0.0001
    e2 = 0.0001
    dst = [0, 0]
    moveTime = 2
    sleepTime = 7
    while True:
        try:
            w = 2
            forwards(0)
            right(0)
            for i in range (1,sleepTime):
                loc = getCor(gps.get_gpgga())
                time.sleep(1)
            loc = getCor(gps.get_gpgga())
            print(dst[0]-loc[0])
            print(dst[1]-loc[1])
            if(abs(dst[0]-loc[0]) > e1):
                w = w - 1
                if(dst[0] > loc[0]):
                    print('f')
                    forwards(200)
                else:
                    print('b')
                    backwards(200)
            if(abs(dst[1]-loc[1]) > e2):
                w = w - 1
                if(dst[1] > loc[1]):
                    print('r')
                    right(100)
                else:
                    print('l')
                    left(100)
            if w == 2:
                print('yay!')
                time.sleep(5)
            time.sleep(moveTime)
        except IOError:
            print('io')
            time.sleep(1)
