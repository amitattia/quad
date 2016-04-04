import time
import microstacknode.hardware.gps.l80gps

if __name__ == '__main__':
    gps = microstacknode.hardware.gps.l80gps.L80GPS()
    while True:
        data = gps.get_gpgga()
        print(data.keys(), data.values())
        time.sleep(1)
