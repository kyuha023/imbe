import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.cleanup() #GPIO 모듈의 점유 리소스를 해제
GPIO.setmode(GPIO.BCM) #핀 번호 지정을 브로드컴칩의 번호를 참조 

# read data using pin 21
instance = dht11.DHT11(pin=21)

result = instance.read()
if result.is_valid():
    print("Last valid input: " + str(datetime.datetime.now()))
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)

 
