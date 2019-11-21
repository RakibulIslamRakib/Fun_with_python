'''we have to install pyaudio and speech_recognition module for this'''
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print('Speach anything')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('You said {}'.format(text))
    except:
        print('Sorry! we could not recognize your voice')

