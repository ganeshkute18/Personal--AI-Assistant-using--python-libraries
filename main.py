import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from gtts import gTTS
import pygame
import os
import pywhatkit  # Import pywhatkit for YouTube search and play
import time  # Import time for deactivation timer

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "<Your Key Here>"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def processCommand(c):
    if c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        speak(f"Searching and playing {song} on YouTube")
        pywhatkit.playonyt(song)
    elif c.lower().startswith("search"):
        query = c.lower().replace("search", "").strip()
        speak(f"Searching for {query} on Google")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Initializing JARVIS....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for the wake-word...")
                audio = recognizer.listen(source)
                wake_word = recognizer.recognize_google(audio)

                if "jarvis" in wake_word.lower():  # Wake-word check remains case-insensitive
                    speak("Yes, I am listening...")
                    start_time = time.time()

                    while True:
                        elapsed_time = time.time() - start_time
                        if elapsed_time > 3:
                            speak("Deactivating...")
                            break

                        print("Listening for your command...")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        print(f"You said: {command}")
                        processCommand(command)
        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, I didn't catch that. Please try again.")
