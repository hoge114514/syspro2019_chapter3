import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)


while (True) :
    GPIO.output(14, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(14, GPIO.LOW)
    time.sleep(0.5)

GPIO.cleanup()
