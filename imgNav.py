import picamera
import opencv2

def getCenter(image):
	return ndimage.measurements.center_of_mass(image)

def imgVec(cam):
    stream = picamera.Array.PiRGBArray(cam)
    camera.capture(stream, format='bgr')
    frame = stream.array
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	res = cv2.bitwise_and(frame,frame, mask=mask)
	cFloat = getCenter(mask)
	if not math.isnan(cFloat[0]):
		c = (int(cFloat[1]), int(cFloat[0]))
        return c
    return (-1, -1)
