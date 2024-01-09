import speech_recognition as sr
# google speech recognition



def file_recognition(file):
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        print("Listening from audio")
        audio_data = r.record(source)
        query = r.recognize_google(audio_data, language='en-US')
        print(f"User said: {query}\n")
    

def microphone_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic)
        audio_data = r.listen(mic, timeout=5)
        query = r.recognize_google(audio_data, language='en-US')


# filename = "public/16-122828-0002.wav"
filename = "public/go_forward.wav"
# filename = "public/stop.wav"

file_recognition(file=filename)