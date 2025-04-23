from utils.recognizer import listen_for_wake_word, get_command
from utils.speaker import speak
from features.open_close import open_software, close_software
from features.time_info import tell_time
from features.custom_commands import handle_custom_commands
import sys

speak("Voice Assistant Initialized. Say 'Jarvis' to wake me up!")

while True:
    if listen_for_wake_word():
        while True:
            command = get_command()
            if command:
                if 'stop' in command:
                    speak('Stopping the program. Goodbye!')
                    sys.exit()
                elif 'open' in command:
                    software = command.replace('open', '').strip()
                    open_software(software)
                elif 'close' in command:
                    software = command.replace('close', '').strip()
                    close_software(software)
                elif 'time' in command:
                    tell_time()
                else:
                    handle_custom_commands(command)
