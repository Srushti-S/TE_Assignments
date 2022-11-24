import time
import board
import RPi.GPIO as GPIO
import adafruit_dht as abc

dhtDevice=abc.DHT22(board.D18)
GPIO.setup(18,GPIO.IN)
GPIO.setup(4,GPIO.OUT)

while True:
    try:
        temperature = dhtDevice.temperature
        humidity=dhtDevice.humidity
        print("Temp={0:0.1f}*C Humidity ={1:0.1f}%".format(temperature, humidity))
        if temperature>25:
            GPIO.output(4,True)
            time.sleep(1)
        GPIO.output(4,False)
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(6.0)