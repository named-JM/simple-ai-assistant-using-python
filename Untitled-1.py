import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('Clearing background noises..Please wait')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('ask me anything...')
        recordedaudio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(recordedaudio)
        print("You said:", text)
        
        if 'search' in text:
            search_query = text.replace('search', '')
            a = f'Searching {search_query}'
            engine.say(a)
            engine.runAndWait()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            
        elif 'time' in text:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            print(current_time)
            engine.say(current_time)
            engine.runAndWait()
            
        elif 'play' in text:
            a = 'Opening YouTube..'
            engine.say(a)
            engine.runAndWait()
            query = text.replace('play', '')
            pywhatkit.playonyt(query)
            
        elif 'youtube' in text:
            b = 'Opening YouTube'
            engine.say(b)
            engine.runAndWait()
            webbrowser.open('https://www.youtube.com')
            
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except Exception as ex:
        print("Error:", ex)

while True:
    cmd()
