# Author: Mohd Rafey Shamim Khan
# Date: 30 April

import speech_recognition as sr     # For speech recognition from microphone
import webbrowser                   # For opening web pages
import pyttsx3                      # For text-to-speech output
import client                       # Placeholder if you have other client usage (can be removed if unused)
from google import genai           # Google's Gemini AI model integration

# Initialize the recognizer and the text-to-speech engine
recognizeEngine = sr.Recognizer()
ttsxEngine = pyttsx3.init()

# Configure voice settings (voices[1] is usually female, voices[0] male)
voices = ttsxEngine.getProperty('voices')
ttsxEngine.setProperty('voice', voices[1].id)

def speak(text):
    """
    Convert text to speech using pyttsx3.
    """
    ttsxEngine.say(text)
    ttsxEngine.runAndWait()

def aiprocessEngine(message):
    """
    Uses Google's Gemini AI to generate content for a given message
    and speaks the AI's response.
    """
    client = genai.Client(api_key="YOUR_API_KEY_HERE")  # Replace with your actual API key

    response = client.models.generate_content(
        model="gemini-2.0-flash",      # Using Gemini 2.0 Flash model
        contents=message               # Passing the user's message as input
    )
    
    speak(response.text)               # Speaking out the AI's response

def processCommand(c):
    """
    Processes the spoken command:
    - Opens websites if known command is given
    - Otherwise passes the command to Gemini AI
    """
    print(c)
    if "open google" in c.lower():
        webbrowser.open('https://www.google.com/')  # You can add more commands using elif
    else:
        aiprocessEngine(c)

if __name__ == "__main__":
    speak("Initializing Jarvis....")   # Startup message
    while True:
        r = sr.Recognizer()

        try:
            # Use microphone to listen for trigger word
            with sr.Microphone() as source:
                print("Listening!!!")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                word = r.recognize_google(audio)
                print(word)

                # If user says "Jarvis", activate assistant
                if word.lower() == 'jarvis':
                    speak("Yes?")
                    print('Jarvis active')

                    # Listen for the actual command
                    with sr.Microphone() as source:
                        print('Recognizing!!!')
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        processCommand(command)

        # Handle errors during speech recognition
        except sr.WaitTimeoutError:
            print("Nothing said!!!")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Recognition error; {0}".format(e))
