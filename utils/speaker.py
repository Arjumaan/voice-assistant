import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get the available voices from the engine
voices = engine.getProperty('voices')

# Set the voice to female (use voices[0] for male voice if needed)
engine.setProperty('voice', voices[1].id)

# Function to convert text to speech
def speak(text):
    # Print the text to the console (for debugging or logging purposes)
    print(f"Jarvis: {text}")
    
    # Use the text-to-speech engine to say the text
    engine.say(text)
    
    # Wait for the speech to finish before continuing
    engine.runAndWait()
