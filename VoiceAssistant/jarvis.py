import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import requests  
import threading  
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

#to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#for greeting
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")

#for weather
def get_hourly_weather_data():
    api_key = "15efa7eab9601230f35e572077b8d6f9"  
    city_id = "524901"  
    while True:  
        data = get_weather_data(api_key, city_id)  
        report = create_weather_report(data)  
        speak(report)  
        break

#for process response data
def create_weather_report(data):  
    report = "Weather Report:\n"  
    city = data["name"]  
    report += f"City: {city}\n"  
    temperature = data["main"]["temp"]  
    report += f"Temperature: {temperature}°C\n"  
    humidity = data["main"]["humidity"]  
    report += f"Humidity: {humidity}%\n"  
    wind_speed = data["wind"]["speed"]  
    report += f"Wind Speed: {wind_speed} m/s\n"  
    return report

#to get weather data     
def get_weather_data(api_key, city_id):  
    api_url = "http://api.openweathermap.org/data/2.5/weather"  
    params = {  
        "id": city_id,  
        "units": "metric",  
        "appid": api_key  
    }  
    response = requests.get(api_url, params=params)  
    data = response.json()  
    return data  

#for process the command
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
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
  
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\motivationalsongs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'the climate':
            thread = threading.Thread(target=get_hourly_weather_data)  
            thread.start()
        elif 'stop' in query:
            speak("bye take care sir............")
            break
