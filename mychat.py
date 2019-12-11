
from flask import Flask, request, jsonify
import sys
import os
import re
import dht11
import time
import datetime
import picamera
import RPi.GPIO as GPIO
import paho.mqtt.publish as publish

app = Flask(__name__)
GPIO.setwarnings(False)
#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
instance = dht11.DHT11(pin=21)
@app.route('/keyboard')
def Keyboard():
    dataSend = {}
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
    work= '오류입니다'
    nowplace = 0
    content = request.get_json()
    content = content['userRequest']
    utterance = content['utterance']
    if utterance == "자리 있어?" :
        nowplace = 0
        camera = picamera.PiCamera()
        camera.resolution = (600, 800)
        camera.capture('ex1.jpg')
        camera.close()
        come='curl -X POST -u "apikey:rTPcDZUHnegT9yLjj3iGNABlYYk0JToqzf7T2kWf24n0" -F "features=objects" -F "collection_ids=64e568a1-96c1-488a-b26c-8c61c6d95f0a" -F "images_file=@ex1.jpg" "https://gateway.watsonplatform.net/visual-recognition/api/v4/analyze?version=2019-02-11"';
        result = os.popen(come)
        mygg = result.read()
        regex = re.compile("location")
        i=0
        re.search("location",mygg)
        if 0 != len(regex.findall(mygg)):
            work = "자리 있습니다"
        else:
            work = "자리 없습니다"
        #print(len(regex.findall(mygg)))

    elif utterance == "온도 알려줘" :
        result = instance.read()
        if result.is_valid():
            work = str(result.temperature)+'도 입니다.'
        else:
            work = '잠시만 기다려주십시오'
            
    elif utterance == "날짜 알려줘" :
        result = instance.read()
        if result.is_valid():
            work = str(datetime.datetime.now())
        else:
            work = '잠시만 기다려주십시오'
            
    elif utterance == "자리 위치 알려줘" :
        nowplace = 0 
        camera = picamera.PiCamera()
        camera.resolution = (600, 800)
        camera.capture('ex1.jpg')
        camera.close()
        come='curl -X POST -u "apikey:rTPcDZUHnegT9yLjj3iGNABlYYk0JToqzf7T2kWf24n0" -F "features=objects" -F "collection_ids=64e568a1-96c1-488a-b26c-8c61c6d95f0a" -F "images_file=@ex1.jpg" "https://gateway.watsonplatform.net/visual-recognition/api/v4/analyze?version=2019-02-11"';
        result = os.popen(come)
        mygg = result.read()
        regex = re.compile("location")
        regex1 = re.compile('object": "1"')
        regex2 = re.compile('object": "2"')
        regex3 = re.compile('object": "3"')
        regex4 = re.compile('object": "4"')
        re.search("location",mygg)
        
        nowplace = len(regex.findall(mygg))
        if 0 != len(regex.findall(mygg)) :
            work = ''
            if 0 != len(regex1.findall(mygg)):
                work=work+'1 '
            if 0 != len(regex2.findall(mygg)):
                work=work+'2 '
            if 0 !=len(regex3.findall(mygg)):
                work=work+'3 '
            if 0 !=len(regex4.findall(mygg)):f
                work=work+'4 '

            work=work+'번 자리가 있습니다'
        else:
            work = "자리가 없습니다"

    elif utterance == "자리 생기면 알려줘":
        while True:
            camera = picamera.PiCamera()
            camera.resolution = (600, 800)
            camera.capture('ex1.jpg')
            camera.close()
            come = 'curl -X POST -u "apikey:rTPcDZUHnegT9yLjj3iGNABlYYk0JToqzf7T2kWf24n0" -F "features=objects" -F "collection_ids=64e568a1-96c1-488a-b26c-8c61c6d95f0a" -F "images_file=@ex1.jpg" "https://gateway.watsonplatform.net/visual-recognition/api/v4/analyze?version=2019-02-11"';
            result = os.popen(come)
            mygg = result.read()
            regex = re.compile("location")
            i = 0
            re.search("location", mygg)
            if 0 != len(regex.findall(mygg)):
                publish.single("ku/mqtt/test", "good", hostname="test.mosquitto.org")
                work = "자리가 생겼습니다"
                break

    print(work)
    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                "simpleText": {
                    "text" : work
                    }

                }
            ]
        }
    }
    print(dataSend)
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10035, debug=True) 
