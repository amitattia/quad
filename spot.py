import time
import microstacknode.hardware.gps.l80gps
import smbus
bus = smbus.SMBus(1)
address = 0x04

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

def getCor(data):
    if data['altitude'] == '':
        return (data['latitude'], 0, data['longitude'])
    cor = (data['latitude'], float(data['altitude']), data['longitude'])
    return cor

if __name__ == '__main__':
    gps = microstacknode.hardware.gps.l80gps.L80GPS()
    #e1 = 0
    #e2 = 0
    e1 = 0.00007
    e2 = 0.00007
    dst = (31.7702385, 770.813999, 35.1974727) 
    while True:
        try:
            bus.write_block_data(address, 2, [0, 4, 0])
            time.sleep(0.2)
            bus.write_block_data(address, 2, [1, 4, 0])
            time.sleep(0.2)
            time.sleep(4)
            loc = getCor(gps.get_gpgga())
            print(dst)
            print(loc)
            if(abs(dst[0]-loc[0]) > e1):
                if(dst[0] > loc[0]):
                    print('f')
                    forwards()
                else:
                    print('b')
                    backwards()
            if(abs(dst[1]-loc[1]) > e2):
                if(dst[2] > loc[2]):
                    print('l')
                    left()
                else:
                    print('r')
                    right()
            time.sleep(3)
        except KeyboardInterrupt:
            print('ctrl+c')
            zero()
            exit()
        except:
            print("io")
            time.sleep(1)
