import speech_recognition as sr
from gtts import gTTS
import os

r=sr.Recognizer()

mic = sr.Microphone()
while True:
    with mic as source:
        audio = r.listen(source)
        nameString = "안녕하세요"
        tts = gTTS(text=nameString, lang='ko')
        tts.save('my.mp3')
        os.system('my.mp3')
    print(r.recognize_google(audio,language='ko-KR'))