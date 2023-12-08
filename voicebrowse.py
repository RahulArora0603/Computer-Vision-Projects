import pyttsx3
import speech_recognition as sr
import webbrowser
import os
#import cv2

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query



if __name__ == '__main__':

    input_command = ["hello jarvis","how are you","i am fine thank you","jarvis recite alphabet","bolo sache darbar ki", "sare bolo"]
    output_command = ["Hello Sir","I am fine. How are you?","A beautiful day, isn't it.","A B C D E F G H I J K L M N O P Q R S T U V W X Y Z","Jai","Jai Mata Di"]
    sites = ['youtube','google','amazon','kaggle','hackerrank','bing','udemy','wikipedia']
    
    speak("assistance activated ")
    speak("How can i help you")
    while True:
        query = take_command().lower()
        if query in input_command:
            sno = input_command.index(query)
            speak(output_command[sno])
        elif "close" in query:
            exit(0)
        elif "open" in query:
            site = query.split(" ")[1]
            if site in sites:
                webbrowser.open(f"{site}.com")
                