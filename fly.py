import smbus
import time
import microstacknode.hardware.gps.l80gps
bus = smbus.SMBus(1)
address = 0x04
def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def all():
    bus.write_block_data(address, 2, [0, 1, 107])
    bus.write_block_data(address, 2, [1, 1, 107])
    bus.write_block_data(address, 2, [2, 1, 107])
    bus.write_block_data(address, 2, [3, 6, 148])

def zero():
    tmp = 0.2
    bus.write_block_data(address, 2, [1, 4, 0])
    time.sleep(tmp)
    bus.write_block_data(address, 2, [0, 4, 0])
    time.sleep(tmp)
    bus.write_block_data(address, 2, [2, 4, 0])
    time.sleep(tmp)
    bus.write_block_data(address, 2, [3, 4, 0])
    time.sleep(tmp)

def up():
    bus.write_block_data(address, 2, [2, 4, 100])
    time.sleep(0.2)

def down():
    bus.write_block_data(address, 2, [2, 3, 100])
    time.sleep(0.2)

def forwards():
    bus.write_block_data(address, 2, [1, 4, 250])
    time.sleep(0.2)

def backwards():
    bus.write_block_data(address, 2, [1, 3, 100])
    time.sleep(0.2)

def right():
    bus.write_block_data(address, 2, [0, 3, 100])
    time.sleep(0.2)

def cool():
    zero()
    all()
    time.sleep(3)
    zero()
    up()
    time.sleep(4)
    down()
    time.sleep(6)
    all()
    time.sleep(3)
    zero()

def enter():
    zero()
    raw_input()
    all()
    raw_input()
    zero()
    up()
    raw_input()
    down()
    raw_input()
    all()
    raw_input()
    zero()

#enter()
    
#all()
#zero()
#up()
#down()

#all()
#time.sleep(3)
#zero()
#up()
#time.sleep(3)
#zero()
#bus.write_block_data(address, 2, [1, 6, 100])
#time.sleep(6)
#zero()
#down()
#time.sleep(6)
#zero()
#all()
#time.sleep(3)
#zero()

#cool()
t = 1
gps = microstacknode.hardware.gps.l80gps.L80GPS()
while True:
    try:
        dst = gps.get_gpgga()
        print('z')
        zero()
        time.sleep(0.2)
        print('f')
        forwards()
        time.sleep(2)
        print('b')
        backwards()
        time.sleep(0.5)
    except KeyboardInterrupt:
        print('ctrl+c')
        zero()
        time.sleep(1)
        exit()
    except:
        print("io")
        time.sleep(1)
zero()
