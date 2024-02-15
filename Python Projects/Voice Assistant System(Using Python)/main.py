import speech_recognition as sr
import os
import webbrowser
import datetime

# def say(text):
#     os.system(f"say {text}")
import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1  #second of non speaking audio for completness
        audio=r.listen(source)
        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language="en-in")
            print(f"User said:{query}")
            return query
        except Exception as e:
            return "Some Error occured"
  
        
        



if __name__=='__main__':
    print('pycharm')
    say("Hello I am Jarvis AI")
    while True:
        print("Listening...")
        query=takecommand()

        #todo:ADD more sites
        sites=[['youtube','https://youtube.com'],['Facebook','https://Facebook.com'],['Wikepedia','https://Wikepedia.com'],
               ['Google','https://Google.com']]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} ...")
                webbrowser.open(site[1])

                #todo:ADD feature to play specfic music
            if " open music" in query:
                path="D:\python\project\Jarvis\pyaudio\o Chives - Royalty (Don Diablo Remix) [NCS Release].mp3"
                os.system(f"open {path}")
            if"the time"  in query:
                strfTime=datetime.datetime.now().strftime("%H:%M:%S")
                say(f"The Time is {strfTime}")
            
            # if "open todolist".lower() in query.lower():
            #     os.system(f"path") --for opening any app just paste location for the app

