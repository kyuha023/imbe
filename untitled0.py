import os
import time
import picamera
import re
        
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

def on_connect(client, userdata, flags, rc):
    client.subscribe("my/mqtt/pict")
    
def on_message(client, userdata, msg):
    print("ggggg")

    
if __name__ == "__main__" :
    nowplace = 0
    try:
        while True:
            camera = picamera.PiCamera()
            camera.resolution = (800, 600)
            camera.capture('ex1.jpg')
            camera.close()
 
            try:
                result = re.findall("place",result)
                print(result)
                nowplace=len(result)
            except Exception:
                nowplace = 0
                
            client = mqtt.Client()
            client.on_connect = on_connect
            client.on_message = on_message
            client.connect("test.mosquitto.org", 1883, 60)
            client.loop_forever()
    
            time.sleep(20)
    except KeyboardInterrupt:
        exit()


