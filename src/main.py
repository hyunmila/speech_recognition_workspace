import speech_recognition as sr
# google speech recognition



def main(mode, file):

    r = sr.Recognizer()
    if mode==0:
        # from file
        with sr.AudioFile(file) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data)
            print(text)
    
    elif mode==1:
        # from microphone # TODO: rn not working - issues with kvm
        with sr.Microphone() as source:
            audio_data = r.record(source, duration=5)
            text = r.recognize_google(audio_data)
            print(text)
    


# filename = "public/16-122828-0002.wav"
filename = "public/go_forward.wav"
filename = "public/stop.wav"

main(mode=0, file=filename)