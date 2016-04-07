import time
import smbus
bus = smbus.SMBus(1)
address = 0x04

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
