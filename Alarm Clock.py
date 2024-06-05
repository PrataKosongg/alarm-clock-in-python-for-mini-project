import time
from datetime import datetime
try:
    from playsound import playsound
    PLAYSOUND_AVAILABLE = True
except ImportError:
    PLAYSOUND_AVAILABLE = False

def set_alarm(alarm_time, notification_type):
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            if notification_type == 'sound' and PLAYSOUND_AVAILABLE:
                playsound('alarm.mp3')  # Ensure you have an 'alarm.mp3' file in the same directory
            else:
                print("It's time to wake up!")
            break
        time.sleep(1)

def main():
    alarm_time = input("Enter the alarm time (HH:MM): ")
    notification_type = input("Do you want to play a sound or display a message? (sound/message): ").lower()
    
    if notification_type == 'sound' and not PLAYSOUND_AVAILABLE:
        print("playsound library is not installed. Defaulting to message notification.")
        notification_type = 'message'
    
    set_alarm(alarm_time, notification_type)

if __name__ == "__main__":
    main()
