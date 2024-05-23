//This Python voice assistant application uses speech recognition and text-to-speech capabilities to perform various tasks based on user voice commands. It leverages the speech_recognition and pyttsx3 libraries for speech input and output, respectively.

Features
1.Open Websites: Opens YouTube or Google upon request.
2.Time Announcements: Tells the current time.
3.Weather Information: Provides weather details for a specified city using the OpenWeatherMap API.
4.Play Music: Plays music from a specified directory.
5.Voice Interaction: Continuously listens for user commands and performs corresponding actions.

  
Usage
Run the script and interact with the assistant by giving voice commands such as "open YouTube," "what's the time," or "play music."//




import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import requests

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for audio input and recognize speech"""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except sr.UnknownValueError:
        print("Could not understand audio")
        return "None"
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
        return "None"
    return query.lower()

def open_website(url):
    """Open a website"""
    webbrowser.open(url)
    speak(f"Opening {url}")

def get_weather(city):
    """Fetch and speak the weather information"""
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        main = weather_data["main"]
        temperature = main["temp"]
        weather_desc = weather_data["weather"][0]["description"]
        speak(f"The temperature in {city} is {temperature - 273.15:.2f} degrees Celsius with {weather_desc}.")
    else:
        speak("City not found.")

def get_time():
    """Fetch and speak the current time"""
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

def play_music():
    """Play music from a specified directory"""
    music_dir = 'YOUR_MUSIC_DIRECTORY_PATH'
    songs = os.listdir(music_dir)
    if songs:
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Playing music.")
    else:
        speak("No music files found in the directory.")

def perform_task(query):
    """Perform tasks based on the recognized query"""
    if 'open youtube' in query:
        open_website("https://www.youtube.com")
    elif 'open google' in query:
        open_website("https://www.google.com")
    elif 'time' in query:
        get_time()
    elif 'weather' in query:
        speak("Which city?")
        city = listen()
        if city != "None":
            get_weather(city)
    elif 'play music' in query:
        play_music()
    elif 'exit' in query:
        speak("Goodbye!")
        exit()
    else:
        speak("I didn't understand that command. Please try again.")

if _name_ == "_main_":
    speak("How can I assist you today?")
    while True:
        query = listen()
        if query and query != "None":
            perform_task(query)
