import sys
import time
import picamera
import imgNav
import smbus
bus = smbus.SMBus(1)
address = 0x04

def getDis(movement, cam=None):
    """Returns a tuple (x-lr,y-fb) distances."""
    if movement == 'gps':
        print('Empty')
        return (0, 0)
    if movement == 'img':
        return imgNav.imgVec(cam)
    if movement == 'test':
        print('Insert distance')
        lr = float(input('lr value: '))
        fb = float(input('fb value: '))
        return (lr, fb)

def lr_move(offset, movement):
    if(offset > 0):
        bus.write_block_data(address, 2, [0, 4, 100])
        print('l')
    else:
        bus.write_block_data(address, 2, [0, 3, 100])
        print('r')
    return

def fb_move(offset, movement):
    if(offset > 0):
        bus.write_block_data(address, 2, [1, 4, 100])
        print('f')
    else:
        bus.write_block_data(address, 2, [1, 3, 100])
        print('b')
    return

if __name__ == "__main__":
    EPSILON = 10**0
    SLEEP = 0.5
    MOVEMENT = sys.argv[1]
    camera = None
    if MOVEMENT == 'img':
        camera = picamera.PiCamera()
    disVec = getDis(MOVEMENT, camera)
    while(sum(x**2 for x in disVec) > EPSILON):
        lr_move(disVec[0], MOVEMENT)
        fb_move(disVec[1], MOVEMENT)
        time.sleep(SLEEP)
        disVec = getDis(MOVEMENT)
    print('Got to location')

