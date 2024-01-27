# Importing necessary libraries/modules
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

# Initializing speech recognition and text-to-speech engines
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to make Alexa speak
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to capture user's voice command
def take_command():
    try:
        # Using a microphone as the audio source
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            # Converting voice to text using Google's speech recognition
            command = listener.recognize_google(voice)
            command = command.lower()
             # Removing the wake word "alexa" from the command
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

# Function to execute different commands based on user input
def run_alexa():
    # Getting user's command
    command = take_command()
    print(command)
    # Performing actions based on recognized command
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
# Getting information about a person from Wikipedia
# Getting a joke using the pyjokes library
# Main loop to keep Alexa running and listening for commands
run_alexa()