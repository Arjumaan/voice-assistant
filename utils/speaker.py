import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # female voice, change to [0] for male

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()
