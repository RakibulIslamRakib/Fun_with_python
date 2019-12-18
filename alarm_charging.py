#It will tell me to plugged in the charger if not charging

import psutil
import pyttsx3

engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

cnt=0  
while True:
    battery = psutil.sensors_battery()
    plugged_in = battery.power_plugged
    charging_percentage = battery.percent
    if not plugged_in:
        speak('Please plug in the charger')
        print("Please plug in the charger")
    else:
        if cnt==0:
            speak('charging')
            print('charging percentage : '+str(charging_percentage))
            cnt=1
        else:
            continue

