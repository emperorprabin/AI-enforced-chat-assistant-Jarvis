from urllib import response
import os
import speech_recognition as sr
import webbrowser
import pyttsx3 
import musiclib
import requests
from google import genai
from openai import OpenAI

#recognizer=sr.Recognizer()
#engine=pyttsx3.init()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine


news_api="6842e38eef034de89bebcbddf02a5832"
speak("Initializing Jarvis...")

if __name__=="__main__":

    while True:
        def ai_build(command):
            client = OpenAI(
                base_url="http://localhost:11434/v1",
                api_key="ollama"  # required by the library, but ignored locally
            )

            response = client.chat.completions.create(
                model="mistral",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant chatbot like siri or alxa. Give clear and short answers."},
                    {"role": "user", "content": command}
                ]
            )

            print(response.choices[0].message.content)
            speak(response.choices[0].message.content)

        def commands(command):
            if "open youtube" in command.lower():
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
            elif "open google" in command.lower():
                speak("Opening Google")
                webbrowser.open("https://www.google.com")

            elif command.lower().startswith("play"):
                song=command.lower().split(" ")[1]
                """link=musiclib.music[song]
                webbrowser.open(link)"""
                if song in musiclib.music:
                    speak(f"Playing {song}")
                    webbrowser.open(musiclib.music[song])
                else:
                    speak(f"Sorry, I don't have {song} in my music library.")
            
            elif "news" in command.lower():
                r=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=6842e38eef034de89bebcbddf02a5832")
                if r.status_code == 200:
                    data = r.json()
                    articles = data["articles"][:5]  # Get the first 5 articles
                    speak("Here are the top news headlines:")
                    for article in articles:
                        speak(article["title"])
            else:
                ai_build(command)
            """elif "exit" in command:
                speak("Exiting Jarvis. Goodbye!")
                break"""
            """else:
                speak("Sorry, I didn't understand that command.")"""
        
        r=sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source)
            command=r.recognize_google(audio)
            print(f"You said: {command}")
            if (command.lower()=="jarvis"):
                speak("Hello, I am Jarvis. How can I assist you?")
                with sr.Microphone() as source:
                    print("Jarvis Is ready...")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    commands(command)
            elif "exit" in command.lower():
                speak("Exiting Jarvis Have a good day")
                break
            """else:
                speak("Sorry, I didn't understand that command.")"""
                #break


        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
