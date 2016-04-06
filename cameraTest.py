import time
import picamera

camera = picamera.PiCamera()
camera.resolution = (640, 480)
try:
    camera.start_preview()
    time.sleep(5)
    camera.stop_preview()
finally:
    camera.close()
