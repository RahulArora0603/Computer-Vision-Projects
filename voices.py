import speech_recognition as sr  
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Kindly voice out your command!")                                                                                   
    audio = r.listen(source)   

try:
    print("Interpreted as: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Apologies, the audio wasn't clear enough.")
except sr.RequestError as e:
    print("There was an issue retrieving results. Error: {0}".format(e))