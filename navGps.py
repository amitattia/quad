import time
import microstacknode.hardware.gps.l80gps
import smbus
bus = smbus.SMBus(1)
address = 0x04

def all():
    bus.write_block_data(address, 2, [0, 1, 107])
    bus.write_block_data(address, 2, [1, 1, 107])
    bus.write_block_data(address, 2, [2, 1, 107])
    bus.write_block_data(address, 2, [3, 6, 148])

def zero():
    bus.write_block_data(address, 2, [0, 4, 0])
    bus.write_block_data(address, 2, [1, 4, 0])
    bus.write_block_data(address, 2, [2, 4, 0])
    bus.write_block_data(address, 2, [3, 4, 0])

def up():
    bus.write_block_data(address, 2, [2, 4, 200])

def down():
    bus.write_block_data(address, 2, [2, 3, 50])

def forwards():
    bus.write_block_data(address, 2, [1, 4, 20])

def backwards():
    bus.write_block_data(address, 2, [1, 3, 50])

def left():
    bus.write_block_data(address, 2, [0, 4, 100])

def right():
    bus.write_block_data(address, 2, [0, 3, 100])

def getCor(data):
	cor = (data['latitude'], data['altitude'], data['longitude'])
	return cor

if __name__ == '__main__':
	gps = microstacknode.hardware.gps.l80gps.L80GPS()
	tmp = 'b'
	#e1 = 0
	#e2 = 0
	e1 = 0.00005
	e2 = 0.00005
	while(tmp != 'a'):
		time.sleep(1)
		dst = getCor(gps.get_gpgga())
		print(dst)
		tmp = input("Press enter..")
	#zero()
	while True:
		try:
			bus.write_block_data(address, 2, [0, 4, 0])
            bus.write_block_data(address, 2, [1, 4, 0])
			time.sleep(0.1)
			loc = getCor(gps.get_gpgga())
			zero()
			if(dst[0]+e1>loc[0]):
				forwards()
			if(dst[0]<e1+loc[0]):
				backwards()
			if(dst[2]+e2>loc[2]):
				left()
			if(dst[2]<e2+loc[2]):
				right()
			time.sleep(1)
		except KeyboardInterrupt:
            print('ctrl+c')
            bus.write_block_data(address, 2, [1, 4, 0])
            bus.write_block_data(address, 2, [0, 4, 0])
            bus.write_block_data(address, 2, [2, 4, 0])
            exit()
		except:
			print("io")
			time.sleep(1)

