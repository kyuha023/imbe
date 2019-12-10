from flask import Flask, request, jsonify
import sys
import os
import re
        
app = Flask(__name__)

@app.route('/keyboard')
def Keyboard():
    dataSend = {}
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
    nowplace = 0
    content = request.get_json()
    content = content['userRequest']
    utterance = content['utterance']
    if utterance == "자리 있어?" :
        camera = picamera.PiCamera()
        camera.resolution = (600, 800)
        camera.capture('ex1.jpg')
        camera.close()
        come='curl -X POST -u "apikey:rTPcDZUHnegT9yLjj3iGNABlYYk0JToqzf7T2kWf24n0" -F "features=objects" -F "collection_ids=64e568a1-96c1-488a-b26c-8c61c6d95f0a" -F "images_file=@myimg.jpg" "https://gateway.watsonplatform.net/visual-recognition/api/v4/analyze?version=2019-02-11"';
        result = os.popen(come)
        mygg = result.read()
        regex = re.compile("location")
        i=0
        re.search("location",mygg)
        len(regex.findall(mygg))

    elif utterance == "자리 생기면 알려줘" :
        while True:
            camera = picamera.PiCamera()
            camera.resolution = (600, 800)
            camera.capture('ex1.jpg')
            camera.close()
            come='curl -X POST -u "apikey:rTPcDZUHnegT9yLjj3iGNABlYYk0JToqzf7T2kWf24n0" -F "features=objects" -F "collection_ids=64e568a1-96c1-488a-b26c-8c61c6d95f0a" -F "images_file=@myimg.jpg" "https://gateway.watsonplatform.net/visual-recognition/api/v4/analyze?version=2019-02-11"';
            result = os.popen(come)
            mygg = result.read()
            regex = re.compile("location")
            i=0
            re.search("location",mygg)
            nowplace = len(regex.findall(mygg))
        	if nowplace != 0 :
        	    break
    elif utterance == "온도 알려줘" :
           
            
    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                "simpleText": {
                    "text" : utterance
                    }
                }
            ]
        }
    }
    return jsonify(dataSend)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10034, debug=True) 