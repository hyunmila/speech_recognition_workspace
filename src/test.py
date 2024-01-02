import speech_recognition as sr
# google speech recognition



def google_reco(file):
    r = sr.Recognizer()
    # from file
    with sr.AudioFile(file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        print(text)
    





# filename = "public/16-122828-0002.wav"
filename = "public/go_forward.wav"
filename = "public/stop.wav"

google_reco(mode=1, file=filename)