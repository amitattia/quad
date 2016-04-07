import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(5)

time.sleep(1)

for i in range(5):
    pwm.ChangeDutyCycle(i*30)
    time.sleep(2)
