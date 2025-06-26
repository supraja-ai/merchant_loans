import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Test TTS
speak("Hello! How can I assist you today?")
