# Importing necessary libraries/modules
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import json

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

# Function to make Alexa greet the user
def greet_user():
    talk('Hello! How can I assist you today?')

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
        print(time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
    # Getting information about a person from Wikipedia
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
    # Getting a joke using the pyjokes library
        talk(pyjokes.get_joke())
    elif 'search' in command:
        search_query = command.replace('search', '')
        talk('Searching for ' + search_query)
        webbrowser.open_new_tab('https://www.google.com/search?q=' + search_query)
    elif 'reminder' in command:
        talk('What should I remind you about?')
        reminder_text = take_command()
        talk('When should I remind you about ' + reminder_text + '?')
        reminder_time = take_command()
        talk(f"Sure! I'll remind you about {reminder_text} at {reminder_time}.")
    else:
        talk('Please say the command again.')

# Main loop to keep Alexa running and listening for commands
while True:
    # Greet the user at the beginning of each iteration
    greet_user() 
# Main loop to keep Alexa running and listening for commands
    run_alexa()