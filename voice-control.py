import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

engine = pyttsx3.init()
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def get_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Listening for command...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}\n")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Could not connect to the speech service.")
        return ""

def perform_action(command):
    if "open browser" in command or "open google" in command:
        speak("Opening browser...")
        webbrowser.open("https://www.google.com")
    
    elif "what's the time" in command or "tell me the time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    
    elif "play music" in command:
        speak("Playing music from your system...")
        music_folder = "C:\\Users\\YourUsername\\Music"  
        songs = os.listdir(music_folder)
        if songs:
            os.startfile(os.path.join(music_folder, songs[0]))
        else:
            speak("No music files found.")
    
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False

    else:
        speak("Sorry, I can't do that yet.")
    
    return True
speak("Hi, I am your voice assistant. How can I help you?")

while True:
    user_command = get_voice_command()
    if user_command:
        should_continue = perform_action(user_command)
        if not should_continue:
            break
