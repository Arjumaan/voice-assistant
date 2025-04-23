import subprocess
import os
from utils.speaker import speak

def open_software(software_name):
    if 'chrome' in software_name:
        speak('Opening Chrome...')
        program = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])

    elif 'microsoft edge' in software_name:
        speak('Opening Microsoft Edge...')
        program = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        subprocess.Popen([program])

    elif 'notepad' in software_name:
        speak('Opening Notepad...')
        subprocess.Popen(['notepad.exe'])

    elif 'calculator' in software_name:
        speak('Opening Calculator...')
        subprocess.Popen(['calc.exe'])

    else:
        speak(f"Sorry, I couldn't find the software named {software_name}.")

def close_software(software_name):
    if 'chrome' in software_name:
        speak('Closing Chrome...')
        os.system("taskkill /f /im chrome.exe")

    elif 'microsoft edge' in software_name:
        speak('Closing Microsoft Edge...')
        os.system("taskkill /f /im msedge.exe")

    elif 'notepad' in software_name:
        speak('Closing Notepad...')
        os.system("taskkill /f /im notepad.exe")

    elif 'calculator' in software_name:
        speak('Closing Calculator...')
        os.system("taskkill /f /im calculator.exe")

    else:
        speak(f"I couldn't find any open software named {software_name}.")
