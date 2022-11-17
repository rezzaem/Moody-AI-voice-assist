#pip install pyttsx3
import pyttsx3
import datetime
pip install SpeechRecognition
import speech_recognition as sr
#pip install wikipedia
import wikipedia
import webbrowser
import tkinter as tk
# from playsound import playsound as ps

engine = pyttsx3.init()
voices = engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id) #changing index changes voices. o for

def speak(text):
  print(f'[Moody]: {text}')
  engine.say(text)
  engine.runAndWait()

def wish_me():
  hour = int(datetime.datetime.now().hour)
  greeting = ''

  if hour>=0 and hour<12:
    greeting = 'Good morning!'
  elif hour>=12 and hour<18:
    greeting = 'Good afternoon!'
  else:
    greeting = 'Good evening!'

  # ps('C:/Users/turbo/Desktop/moody01.mp3')

  speak(f'{greeting} I am Moody , the smart assisstant of Reza . How may I help you today?')

def takeCommand():
  #It takes microphone input from the user and returns string output
  r = sr.Recognizer() 
  with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

  try:
    print("Recognizing...")    
    query = r.recognize_google(audio, language='en-in')
    print(f"[Me]: {query}")

  except Exception as e:
    # print(e)    
    return "None"
  return query



# script starts here

wish_me()

while True:
# if 1:
  query = takeCommand().lower()

  # Logic for executing tasks based on query
  query = query.replace('Moody', '')

  if 'exit' in query:
    speak('Goodbye!')
    exit()

  elif 'hello' in query:
    speak('Hello there!')
  
  elif 'cow' in query:
    speak('I am a robot, I do not have judjement but according to the wikipedia , the result is mohammad behroozi or mambozi.')
  
  elif 'goodbye' in query:
    speak('Goodbye!')
    exit()

  elif 'thank you' in query:
    speak('You are welcome!')

  elif 'wikipedia' in query:
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    query = query.replace("search", "")
    query = query.replace("for", "")
    results = wikipedia.summary(query, sentences=1)
    speak(f'According to Wikipedia, {results}')

  elif 'open youtube' in query:
    speak('Opening Youtube')
    webbrowser.open("https://youtube.com")

  elif 'google' in query and 'search' in query:
    speak('Searching Google...')
    query = query.replace("google", "")
    query = query.replace("search", "")
    query = query.replace("for", "")
    webbrowser.open(f'https://google.com/search?q={query}')
  elif 'open google' in query:
    speak('Opening Google')
    webbrowser.open("https://google.com")

  elif 'open stack overflow' in query:
    speak('Opening StackOverflow')
    webbrowser.open("https://stackoverflow.com")

  elif 'what' in query and 'time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speak(f"Sir, The time is {strTime}")

  elif 'meaning of life' in query:
    speak('Sir, the meaning of life is 42.')
  
  elif 'how are you' in query:
    speak('I am doing jolly good, sir.')

  else:
    
    speak('I didn\'t quiet catch you sir. Can you please try that again?') 