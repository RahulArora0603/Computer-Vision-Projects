import pyttsx3 #text to speech(TTS) library
import speech_recognition as sr
import mysql.connector
engine = pyttsx3.init("sapi5") #TTS engine
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  #voices[0 - male voice , 1 - female voice] 

#speak function (audio output)-
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#recognize audio input from user -
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
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
    try: #connecting to mysql database
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Rahul@0603"
        )
        mycursor = mydb.cursor()
        mycursor.execute("use train_jarvis")
        speak("Assistance activated ")
        speak("I am ready to learn")
        while True:
            user_query = take_command().lower() #stored as user input 
            my_response = take_command().lower()#stored as computer output
            if (user_query=="close") or (my_response=="close"):
                exit(0)
            if (user_query!="none") and (my_response!="none"):
                try:
                   mycursor.execute(f"insert into robo_commands values(default,'{user_query}','{my_response}');") #saving into database
                   mydb.commit()
                except Exception as ex:
                   print(ex)
                   exit(0)
            
                
    except Exception as e:
        print(e)
        print("Unable to connect to database.")
