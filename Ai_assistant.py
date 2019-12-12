import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from random import randint
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


emaildict = {'dog': 'jahincse14@gmail.com','moon':'munimhossain411@gmail.com','neela':'surayanila7254@gmail.com',
             'imran':'ik21.cse14@gmail.com','dick':'d.m.n.hayder@gmail.com'}

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
    speak('Please tell me how may I help you sir!')


def takeCommand():
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
            speak('Say that again please')
            return 'None'
        return query


def recipient(s):
    index = s.index('to')
    recipient = s[(index+3):]
    return recipient


def sendmail(email, password, to_mail, subject, message):
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = to_mail
    msg['Subject'] = subject
    msg.attach(MIMEText(message,'Plain'))

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email,password)
    text = msg.as_string()
    server.sendmail(email,to_mail,text)
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
            '''
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
            '''

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, The time is {strTime}")

            '''
        elif 'open chrome' in query:
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
            

        #elif 'open code' in query:
         #   path = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
          #  os.startfile(path)
          

        elif 'open powerpoint' in query:
            path = "C:\Rakib\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\CodeBlocks"
            os.startfile(path)
            '''
        elif 'send email' in query:
            to_maile = recipient(query)
            if to_maile in emaildict.keys():
                try:
                    speak('What should i say?')
                    message = takeCommand()
                    email = 'rakibulr312@gmail.com'
                    password = '01791742746'
                    to_mail = emaildict[to_maile]
                    subject = 'this is subject'
                    sendmail(email, password, to_mail, subject, message)
                    speak('Email has been send')
                except Exception as e:
                    print('Sorry! i cant send him email Now Please tru again')
                    speak('Sorry! i cant send him email Now Please tru again')
            else:
                print('Sorry! I dont have {}"s email address. please try again sir!'.format(to_maile))
