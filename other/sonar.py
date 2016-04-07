import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_ECHO = 24

#       print("Ultrasonic Measurement")

# Set pins as output and input
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Allow module to settle
time.sleep(1)

def getD():

        start = time.time()
        while GPIO.input(GPIO_ECHO)==0:
          start = time.time()

        while GPIO.input(GPIO_ECHO)==1:
          stop = time.time()

        # Calculate pulse length
        elapsed = stop-start

        # Distance pulse travelled in that time is time
        # multiplied by the speed of sound (cm/s)
        distance = elapsed * 34000

        # That was the distance there and back so halve the value
        distance = distance / 2

#       print("Distance : %.1f" % distance)
        return distance*1.052

while(1):
	time.sleep(0.5)
	print(getD())
