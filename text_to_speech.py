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
engine.setProperty("voice", voices[0].id) #Voice change
text = '''Just hit 150 followers!Thank you for your support. 
Excited to share more projects, challenges, and insights with you all. 
Let's keep learning and growing together!'''
engine.say(text)
engine.runAndWait()

