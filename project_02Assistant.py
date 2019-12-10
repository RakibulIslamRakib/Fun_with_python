import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from random import randint
import smtplib

emaildict = {'jahin': 'jahincse14@gmail.com','munim':'munimhossain411@gmail.com','hulo':'ik21.cse14@gmail.com','nadim':'d.m.n.hayder@gmail.com'}

engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voice)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 11:
        speak('Good morning sir !')
    elif hour >= 12 and hour <= 15:
        speak('Good afternoon sir !')
    elif hour>=16 and hour<=19:
        speak('Good evening sir !')
    else:
        speak('Good night sir !')
    speak('I am sophia, your assistant. Please tell me how may I help you sir!')


def  takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        #print(f'User said {query}\n')
    except Exception as e:
        print('Say that again please...')
        return 'None'
    return query

def recipient(s):
    index = s.index('to')
    recipient = s[(index+3):]
    return recipient

def sendEmail(to,content):
    server = smtplib.SNTP('sntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rakibulr312@gmail.com','01791742746')
    server.sendmail('rakibulr312@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            print('Searceing wikipedia')
            speak('Searceing wikipedia')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open codeforce' in query:
            webbrowser.open('codeforces.com')
        elif 'open hackerrank' in query:
            webbrowser.open('hackerrank.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query:
            music_dir = 'G:\\Adio\\Music'
            songs = os.listdir(music_dir)
            #print(songs)
            index = randint(0,len(songs)-1)
            songName = songs[index].replace('_',' ')
            songName = songName.replace('mp3',' ')
            songName = songName.replace('.',' ')
            speak(f"Playing {songName} for you sir!")
            os.startfile(os.path.join(music_dir,songs[index]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, The time is {strTime}")

        elif 'open chrome' in query:
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)

        #elif 'open code' in query:
         #   path = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
          #  os.startfile(path)

        elif 'open powerpoint' in query:
            path = "C:\Users\Rakib\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\CodeBlocks"
            os.startfile(path)

        elif 'send email' in query:
            try:
                speak('What shoult i say?')
                content = takeCommand()
                to =  emaildict[recipient(query)]
                sendEmail(to,content)
                speak('Email has been send')
            except Exception as e:
                speak(f'I am sorry for {recipient(query)} I am not able to send him mail this time!')








