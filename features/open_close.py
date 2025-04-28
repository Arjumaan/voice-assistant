import subprocess
import os
from utils.speaker import speak

# Function to open specific software based on the software name
def open_software(software_name):
    if 'chrome' in software_name:
        # Open Google Chrome
        speak('Opening Chrome...')
        program = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])  # Launch the program

    elif 'microsoft edge' in software_name:
        # Open Microsoft Edge
        speak('Opening Microsoft Edge...')
        program = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        subprocess.Popen([program])  # Launch the program

    elif 'notepad' in software_name:
        # Open Notepad
        speak('Opening Notepad...')
        subprocess.Popen(['notepad.exe'])  # Launch the program

    elif 'calculator' in software_name:
        # Open Calculator
        speak('Opening Calculator...')
        subprocess.Popen(['calc.exe'])  # Launch the program

    else:
        # Handle unknown software names
        speak(f"Sorry, I couldn't find the software named {software_name}.")

# Function to close specific software based on the software name
def close_software(software_name):
    if 'chrome' in software_name:
        # Close Google Chrome
        speak('Closing Chrome...')
        os.system("taskkill /f /im chrome.exe")  # Forcefully terminate the process

    elif 'microsoft edge' in software_name:
        # Close Microsoft Edge
        speak('Closing Microsoft Edge...')
        os.system("taskkill /f /im msedge.exe")  # Forcefully terminate the process

    elif 'notepad' in software_name:
        # Close Notepad
        speak('Closing Notepad...')
        os.system("taskkill /f /im notepad.exe")  # Forcefully terminate the process

    elif 'calculator' in software_name:
        # Close Calculator
        speak('Closing Calculator...')
        os.system("taskkill /f /im calculator.exe")  # Forcefully terminate the process

    else:
        # Handle unknown software names
        speak(f"I couldn't find any open software named {software_name}.")
