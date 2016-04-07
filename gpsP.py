import time
import microstacknode.hardware.gps.l80gps
import commandP.py

def getCor(data):
    cor = (data['latitude'], data['longitude'])
    return cor

def gpsNavigation():
    gps = microstacknode.hardware.gps.l80gps.L80GPS()
    e1 = 0.0001
    e2 = 0.0001
    dst = [0, 0]
    while True:
        try:
            w = 2
            bus.write_block_data(address, 2, [0, 4, 0])
            time.sleep(0.2)
            bus.write_block_data(address, 2, [1, 4, 0])
            time.sleep(0.2)
            time.sleep(3)
            loc = getCor(gps.get_gpgga())
            if(abs(dst[0]-loc[0]) > e1):
                w = w - 1
                if(dst[0] > loc[0]):
                    print('f')
                    forwards()
                else:
                    print('b')
                    backwards()
            if(abs(dst[1]-loc[1]) > e2):
                w = w - 1
                if(dst[1] > loc[1]):
                    print('l')
                    left()
                else:
                    print('r')
                    right()
            if w == 2:
                input('Enter to continue...')
            time.sleep(3)
        except IOError:
            print('io')
            time.sleep(1)
