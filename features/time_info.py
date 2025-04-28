import datetime
from utils.speaker import speak

# Function to tell the current time
def tell_time():
    # Get the current time in the format 'HH:MM AM/PM'
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    
    # Print the current time to the console (for debugging or logging purposes)
    print(f"Current Time: {current_time}")
    
    # Use the speak function to audibly announce the current time
    speak(f"The time is {current_time}")
