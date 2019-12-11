import paho.mqtt.client as mqtt
import os
import speech_recognition as sr

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("ku/mqtt/test")

def on_message(client, userdata, msg):
    nameString = "자리가 생겼습니다"


    os.system('omxplayer my.mp3')

if __name__ == '__main__':
    try:
        while True:
            client = mqtt.Client()
            client.on_connect = on_connect
            client.on_message = on_message
            client.connect("test.mosquitto.org", 1883, 60)
            client.loop_forever()
    except KeyboardInterrupt:
        exit()
