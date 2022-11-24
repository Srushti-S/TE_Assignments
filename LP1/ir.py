import RPi.GPIO as GPIO
import time

sensor=11
led=5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

GPIO.output(led, False)

print("IR sensor Ready.....")
print(" ")

time.sleep(5)

try:
    while True:
        if GPIO.input(sensor):
            GPIO.output(led,False)
            print("Object Detetcted")
            while GPIO.input(sensor):
                time.sleep(0.2)
            GPIO.output(led,True)
        else:
            GPIO.output(led,True)
except KeyboardInterrupt:
    GPIO.cleanup()