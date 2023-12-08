import pyttsx3

def onStart(name):
    print('Starting to speak:', name)

def onEnd(name, completed):
    if completed:
        print('Speech completed successfully:', name)
    else:
        print('Speech interrupted:', name)

engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('finished-utterance', onEnd)
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id) #Voice change
x,y = 10,5
z = x*y
engine.say(f"{x} multiplied by {y} = {z}")
engine.runAndWait()