import pyttsx3
import speech_recognition as sr
import mysql.connector #library for connecting to mysql 

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
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Rahul@0603"
        )
        mycursor = mydb.cursor()
        mycursor.execute("use train_jarvis")
        speak("Assistance activated ")
        speak("I am ready to learn")
        mycursor.execute("use train_jarvis")
        comp_input = [] 
        comp_response = []
        mycursor.execute("select * from robo_commands")
        output = mycursor.fetchall() #fetch data from database
        for x in output:
            comp_input.append(x[1]) #inputs stored in jarvis
            comp_response.append(x[2]) #outputs stored in jarvis
        while True:
            user_query = take_command().lower()
            if user_query in comp_input:
                r = comp_input.index(user_query)
                speak(comp_response[r])
            if user_query=="close":
                exit(0)
            else:
                speak("Command not in database.")    
    except Exception as e:
        print(e)
        print("Unable to connect to database.")
