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
        frame = stream.array
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([140,110,90])
        upper_blue = np.array([185,210,160])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        cv2.imshow('mask',mask)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
