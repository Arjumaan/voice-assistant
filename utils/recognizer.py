import speech_recognition as sr

# mic_list = sr.Microphone.list_microphone_names()
# print("Available Microphones:")
# for i, mic_name in enumerate(mic_list):
#     print(f"{i}: {mic_name}")

recognizer = sr.Recognizer()

def listen_for_wake_word(wake_word="jarvis"):
    with sr.Microphone() as source:
        print('Listening for wake word...')
        while True:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            recorded_audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(recorded_audio, language='en-US').lower()
                if wake_word in text:
                    print('Wake word detected!')
                    return True
            except Exception as ex:
                print("Could not understand audio, please try again.")

def get_command():
    with sr.Microphone() as source:
        print('Listening for command...')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        recorded_audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(recorded_audio, language='en-US').lower()
        print(f'Heard: {text}')
        return text
    except Exception as ex:
        print("Could not recognize command:", ex)
        return ""
