import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 21
instance = dht11.DHT11(pin=21)

result = instance.read()
if result.is_valid():
    print("Last valid input: " + str(datetime.datetime.now()))
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)

 