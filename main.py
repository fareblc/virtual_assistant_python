import speech_recognition as sr
import pyttsx3
import os
from pathlib import Path

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text: str):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'maria' in command:
                # talk(command)
                command = command.replace('maria', '')
                print(command)
    except:
        pass
    return str(command)


def run_maria():
    command = take_command()
    if 'open' in command and 'folder' in command:
        fld = command.replace('open', '').replace('folder', '')
        print('Opening ' + fld)
        full_dir = str(Path.home() / fld.strip())
        os.startfile(full_dir)


run_maria()
