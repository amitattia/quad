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

def lift():
    bus.write_block_data(address, 2, [2, 8, 255])
    time.sleep(5)

def cool():
    zero()
    all()
    time.sleep(3)
    zero()
    lift()
    forward()
    time.sleep(2)
    backward()
    time.sleep(1.5)
    for i in range (1,3):
      right()
      time.sleep(0.5*i)
      bacward()
      time.sleep(0.5*i)
      if i==2:
        down()
      else:
        up()
      sleep(0.5)
      left()
      time.sleep(0.5*i)
      forward()
      time.sleep(0.5*i)
      
      
      
      
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
