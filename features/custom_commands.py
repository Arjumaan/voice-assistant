import pywhatkit

# DISABLE connection check
pywhatkit.core.check_connection = lambda: True

from utils.speaker import speak

def handle_custom_commands(command):
    # Play on YouTube
    if 'play' in command:
        query = command.replace('play', '').strip()
        speak(f'Playing {query} on YouTube')
        pywhatkit.playonyt(query)

    # Tell the time (redundant if you like)
    elif 'time' in command:
        # You can import and call tell_time() here
        from features.time_info import tell_time
        tell_time()

    # Your custom questions
    elif 'what is your name' in command:
        speak('My name is Assistant, your voice assistant.')
    elif 'who is god' in command:
        speak('Ajitheyyy Kadavuleyy')

    else:
        speak("Sorry, I didn't understand that command.")