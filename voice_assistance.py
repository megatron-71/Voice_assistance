import pyttsx3
import speech_recognition as sr
import time

engine = pyttsx3.init()

def speak(text):
    print(f"System: {text}")
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.5) 

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand. Please say again.")
        return listen()
    except sr.RequestError:
        speak("Speech service error. Please check your internet connection.")
        return ""

def voice_assistant():
    speak("Hi, I am your assistant.")
    _ = listen()

    speak("What is your name?")
    name = listen()

    speak(f"Nice to meet you, {name}. How can I help you?")
    task = listen()

    if "message" in task.lower() or "mail" in task.lower():
        speak("On what — mail or WhatsApp?")
        platform = listen()

        if "mail" in platform.lower():
            speak("Okay, mail has been composed. Please review.")
            print("=====Mail Content=====")
            print("Dear Aanchal, This is a test message from my voice assistant.")
            print("======================")

            speak("Is it okay?")
            confirm = listen()

            if "yes" in confirm.lower():
                speak("Mail sent successfully!")
            else:
                speak("Mail canceled.")

        elif "whatsapp" in platform.lower():
            speak("WhatsApp message composed. Please confirm.")
            confirm = listen()

            if "yes" in confirm.lower():
                speak("WhatsApp message sent successfully!")
            else:
                speak("Message canceled.")
        else:
            speak("Sorry, I can only send messages via mail or WhatsApp.")

    else:
        speak("Sorry, I can only help with sending messages currently.")

if __name__ == "__main__":
    voice_assistant()