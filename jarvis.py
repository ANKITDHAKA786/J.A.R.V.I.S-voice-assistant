import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import pyjokes
# import smtplib
import pywhatkit
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def joke():
    for i in range(5):
        speak(pyjokes.get_jokes(language="en", category="neutral")[i], sep='\n')

def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Gooda Morning !")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening !")
    
    speak("I am Jarvis Sir, Please tell me how may i help you")

def takeCommand():
    ''' It takes Microphone input from user and return string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 0.6
        r.energy_threshold=494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print("Say that again Please.....")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        '''logic for executing tasks based on query'''
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query=query.replace("wikipedia", "")
            results= wikipedia.summary(query, 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'music' in query:
            music_dir='E:\\mobile\\Download'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")
            
        elif 'open code' in query:
            codePath= "C:\\Users\\Alienware\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'on youtube' in query:
            speak("Ok, Sir !")
            query=query.replace('on youtube', '')
            pywhatkit.playonyt(query)
        
        elif 'joke' in query:
            joke()


        
  