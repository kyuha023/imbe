from flask import Flask, request, jsonify
import sys
app = Flask(__name__)

@app.route('/keyboard')
def Keyboard():
    dataSend = {}
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
    content = request.get_json()
    content = content['userRequest']
    utterance = content['utterance']

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
 app.run(host='0.0.0.0', port=8000, debug=True) 