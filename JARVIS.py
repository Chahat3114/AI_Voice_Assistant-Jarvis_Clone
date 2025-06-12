import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import wikipedia
from gtts import gTTS
import pygame
import time
import os

pygame.mixer.init()

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "827ceeed5c774f908e217c09e3a396f0"

def speak_old(text):
    print("Jarvis says:", text)  # For debug
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    # pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove('temp.mp3')

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif c.startswith("play"):
        song = c.split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}.")
    elif "news" in c:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            data = r.json()
            articles = data.get('articles', [])
            if articles:
                speak("Here are the top headlines:")
                for article in articles:
                    print(article['title'])
                    speak(article['title'])

   
    else:
           try:
               result = wikipedia.summary(c, sentences=2)
               speak(result)
           except wikipedia.exceptions.DisambiguationError as e:
               speak("Your question was a bit unclear. Can you be more specific?")
           except wikipedia.exceptions.PageError:
               speak("Sorry, I couldn't find any information on that.")
           except Exception as e:
               print("Wikipedia Error:", e)
               speak("Something went wrong while searching Wikipedia.")


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'Jarvis'...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                word = recognizer.recognize_google(audio)
                print("Heard:", word)

                if word.lower() == "jarvis":
                    speak("Yes?")
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        print("Command:", command)
                        processCommand(command)

        except sr.WaitTimeoutError:
            continue
        except sr.UnknownValueError:
            continue
        except Exception as e:
            print("Error:", e)
            continue