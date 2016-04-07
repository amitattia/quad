import time
import microstacknode.hardware.gps.l80gps

def getCor(data):
    if data['altitude'] == '':
        return (data['latitude'], 0, data['longitude'])
    cor = (data['latitude'], float(data['altitude']), data['longitude'])
    return cor

if __name__ == '__main__':
    gps = microstacknode.hardware.gps.l80gps.L80GPS()
    while True:
        data = gps.get_gpgga()
        vec = getCor(data)
        print('lat alt long')
        print(vec)
        time.sleep(7)
