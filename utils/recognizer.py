import speech_recognition as sr

# Uncomment the following lines to list available microphones for debugging
# mic_list = sr.Microphone.list_microphone_names()
# print("Available Microphones:")
# for i, mic_name in enumerate(mic_list):
#     print(f"{i}: {mic_name}")

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Function to listen for a specific wake word (default is "jarvis")
def listen_for_wake_word(wake_word="jarvis"):
    with sr.Microphone() as source:
        print('Listening for wake word...')
        while True:
            # Adjust for ambient noise to improve recognition accuracy
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            # Listen to the audio input from the microphone
            recorded_audio = recognizer.listen(source)
            try:
                # Convert the recorded audio to text using Google's speech recognition
                text = recognizer.recognize_google(recorded_audio, language='en-US').lower()
                # Check if the wake word is in the recognized text
                if wake_word in text:
                    print('Wake word detected!')
                    return True
            except Exception as ex:
                # Handle errors if the audio could not be understood
                print("Could not understand audio, please try again.")

# Function to listen for a command after the wake word is detected
def get_command():
    with sr.Microphone() as source:
        print('Listening for command...')
        # Adjust for ambient noise to improve recognition accuracy
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        # Listen to the audio input from the microphone
        recorded_audio = recognizer.listen(source)

    try:
        # Convert the recorded audio to text using Google's speech recognition
        text = recognizer.recognize_google(recorded_audio, language='en-US').lower()
        print(f'Heard: {text}')  # Print the recognized command for debugging
        return text
    except Exception as ex:
        # Handle errors if the command could not be recognized
        print("Could not recognize command:", ex)
        return ""
