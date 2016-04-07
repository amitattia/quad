import time
import picamera
import picamera.array
import cv2

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    time.sleep(2)
    with picamera.array.PiRGBArray(camera) as stream:
        camera.capture(stream, format='bgr')
        # At this point the image is available as stream.array
        image = stream.array
        cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
