import time
import smbus
bus = smbus.SMBus(1)
address = 0x04

def lift():
    bus.write_block_data(address, 2, [2, 6, 148])
    time.sleep(5)

def zero():
    bus.write_block_data(address, 2, [0, 4, 0])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [1, 4, 0])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [2, 4, 0])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [3, 4, 0])
    time.sleep(0.2)

def all():
    bus.write_block_data(address, 2, [0, 1, 107])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [1, 1, 107])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [2, 1, 107])
    time.sleep(0.2)
    bus.write_block_data(address, 2, [3, 6, 148])
    time.sleep(0.2)
    
def maxup():
    bus.write_block_data(address, 2, [2, 6, 148])
    time.sleep(0.2)

def up(p = 100):
    bus.write_block_data(address, 2, [2, 4, p])
    time.sleep(0.2)

def down(p = 100):
    bus.write_block_data(address, 2, [2, 3, 255-p])
    time.sleep(0.2)

def forwards(p = 100):
    bus.write_block_data(address, 2, [1, 4, p])
    time.sleep(0.2)

def backwards(p = 100):
    bus.write_block_data(address, 2, [1, 3, 255-p])
    time.sleep(0.2)

def right(p = 100):
    bus.write_block_data(address, 2, [0, 4, p])
    time.sleep(0.2)

def left(p = 100):
    bus.write_block_data(address, 2, [0, 3, 255-p])
    time.sleep(0.2)
