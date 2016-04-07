import RPi.GPIO as GPIO
import time

def drop():
    time.sleep(1)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    pwm = GPIO.PWM(18, 100)
    pwm.start(5)
    time.sleep(1)
    pwm.ChangeDutyCycle(30)
    time.sleep(1)
    pwm.ChangeDutyCycle(20)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(50)
