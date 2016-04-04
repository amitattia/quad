import picamera
import opencv2

def imgVec(cam):
    with picamera.array.PiRGBArray(cam) as stream:
        camera.capture(stream, format='bgr')
        image = stream.array
    
