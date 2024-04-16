import speech_recognition as sr
from datetime import datetime
import time
r = sr.Recognizer()
text = ''
print(datetime.now())
f=open('D:/python/speech_record_text.txt','a')
while True:
    if 'stop' == text:
        break
    with sr.Microphone() as source:
        print('recording started')
        audio_data = r.record(source,duration=5)
        print("recording ended")
        try:
            text = r.recognize_google(audio_data)
            print(text)
            f.write(str(datetime.now())+": INFO   "+str(text)+'\n')
        except:
            e="audio is not clear"
            print (e)
            f.write(str(datetime.now())+": INFO   "+e+'\n')
            
    time.sleep(2) 