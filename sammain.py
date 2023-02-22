import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pywhatkit
import pyjokes

print('Loading your AI personal assistant -sam')


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("iam your AI personal assistant sam")
wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        elif "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant sam is shutting down,Good bye')
            print('your personal assistant sam is shutting down,Good bye')
            break



        elif 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key="64b766cf443262a707ddcf4979ea9172"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'what is your name' in statement:
            speak("iam sam your voice assistant built and developed by the team tech gs")
        elif 'good morning' in statement:
            speak("good morning have a great day")
        elif 'good afternoon' in statement:
            speak("good afternoon how was your lunch")
        elif 'good evening' in statement:
            speak("good evening how was the day")
        elif 'good night' in statement:
            speak("good night sweet dreams")
        elif 'who is your boss' in statement:
            speak("i was created by the three genious sarathi gokulan gokulaprasaanth")
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am sam version 1 point O your persoanl assistant. I am programmed to minor tasks')
                 

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Tech GS")
            print("I was built by Tech GS")

        elif 'play' in statement: 
            song = statement.replace('play', '')
            speak('Playing....' + song)
            print("Playing....")
            pywhatkit.playonyt(song)

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
        elif 'instagram' in statement:
            news = webbrowser.open_new_tab("https://www.instagram.com/")
            speak('Here we go,opening instagram')
            time.sleep(6)
        elif 'facebook' in statement:
            news = webbrowser.open_new_tab("https://www.facebook.com/")
            speak('Here we go,opening facebook')
            time.sleep(6)
        elif 'shop' in statement:
            news = webbrowser.open_new_tab("https://www.amazon.in/")
            speak('Here we go,opening amazon,happy shopping')
            time.sleep(6)
        elif 'code' in statement:
            news = webbrowser.open_new_tab("https://leetcode.com/")
            speak('Here we go,opening leetcode,let your development begins')
            time.sleep(6)
        elif 'linkedin' in statement:
            news = webbrowser.open_new_tab("https://in.linkedin.com/")
            speak('Here we go,opening linkedin,build your profile ')
            time.sleep(6)
        
        elif 'joke' in statement:
            get_j = pyjokes.get_joke()
            print(get_j)
            speak(get_j)
        
        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"GS camera","img.jpg")

        
        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        
        elif 'what can you do' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'goodbye' in statement:
            speak("Good bye ")
            break

time.sleep(2)