import datetime
import time
import threading
import pygame

# Initialize pygame for sound
pygame.mixer.init()
pygame.mixer.music.load('alarm.wav')

# Function to check and trigger alarms
def check_alarm(alarms):
    while True:
        now = datetime.datetime.now()
        for alarm in alarms:
            if now >= alarm['time'] and not alarm['triggered']:
                print("Alarm: {} - Time to wake up!".format(alarm['time'].strftime('%d/%m/%Y %H:%M:%S')))
                alarm['triggered'] = True
                # Play the beep sound for 5 seconds
                pygame.mixer.music.play()
                time.sleep(5)
                pygame.mixer.music.stop()
        time.sleep(1)  # Check alarms every second

# Function to set a new alarm
def set_alarm():
    date_str = input("Enter the alarm date (dd/mm/yyyy): ")
    time_str = input("Enter the alarm time (hh:mm): ")
    
    try:
        alarm_time = datetime.datetime.strptime(f"{date_str} {time_str}", '%d/%m/%Y %H:%M')
        if alarm_time < datetime.datetime.now():
            print("Invalid time. Please set the alarm for a future time.")
        else:
            alarms.append({'time': alarm_time, 'triggered': False})
            print("Alarm set for: {}".format(alarm_time.strftime('%d/%m/%Y %H:%M')))
    except ValueError:
        print("Invalid date or time format. Please use dd/mm/yyyy and hh:mm.")

# List to store alarm data
alarms = []

# Create a thread to check alarms
alarm_thread = threading.Thread(target=check_alarm, args=(alarms,))
alarm_thread.daemon = True
alarm_thread.start()

while True:
    print("\nOptions:")
    print("Enter 'set' to set a new alarm")
    print("Enter 'list' to list all alarms")
    print("Enter 'quit' to exit the program")
    
    choice = input(": ").lower()
    
    if choice == 'set':
        set_alarm()
    elif choice == 'list':
        print("\nScheduled Alarms:")
        for i, alarm in enumerate(alarms):
            print("{}. {}".format(i + 1, alarm['time'].strftime('%d/%m/%Y %H:%M')))
    elif choice == 'quit':
        break
    else:
        print("Invalid input. Please try again.")
