import datetime
from utils.speaker import speak

def tell_time():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    print(f"Current Time: {current_time}")
    speak(f"The time is {current_time}")
