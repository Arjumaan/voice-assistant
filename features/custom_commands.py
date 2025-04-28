import pywhatkit

# Disable the connection check in pywhatkit to avoid unnecessary errors
pywhatkit.core.check_connection = lambda: True

from utils.speaker import speak

# Function to handle custom commands
def handle_custom_commands(command):
    # Play a video or song on YouTube
    if 'play' in command:
        query = command.replace('play', '').strip()  # Extract the query by removing 'play'
        speak(f'Playing {query} on YouTube')  # Inform the user
        pywhatkit.playonyt(query)  # Use pywhatkit to play the query on YouTube

    # Tell the time (optional, as it may already exist in other features)
    elif 'time' in command:
        # Dynamically import and call the tell_time function
        from features.time_info import tell_time
        tell_time()

    # Respond to the user's custom questions
    elif 'what is your name' in command:
        speak('My name is Assistant, your voice assistant.')  # Respond with the assistant's name
    elif 'who is god' in command:
        speak('Ajitheyyy Kadavuleyy')  # Respond with a custom answer

    # Handle unrecognized commands
    else:
        speak("Sorry, I didn't understand that command.")  # Inform the user about unrecognized input