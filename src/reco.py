import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening from microphone")
        r.adjust_for_ambient_noise(mic)
        audio = r.listen(mic, timeout=5)
    try:
        # print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please...")
        return "None"
    return query

# query = takeCommand().lower()