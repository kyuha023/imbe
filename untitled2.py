from flask import Flask, request, jsonify
import sys
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
        camera.resolution = (800, 600)
        camera.capture('ex1.jpg')
        camera.close()
    elif utterance == "자리 생기면 알려줘" :
        while True:
            camera = picamera.PiCamera()
            camera.resolution = (800, 600)
            camera.capture('ex1.jpg')
            camera.close()
	if nowplace != 0 :
    elif utterance == "온도 알려줘" :
            camera = picamera.PiCamera()
            camera.resolution = (800, 600)
            camera.capture('ex1.jpg')
            camera.close()
            
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