from typing import Optional, Tuple, Union
import customtkinter
from scripts import forward, stop
from src.reco import takeCommand
import speech_recognition as sr
from time import sleep

class TopLevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("HMI - Voice Recognition")
        self.geometry("400x300")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0,1), weight=1)
        self.speaking_button = customtkinter.CTkButton(self, text="start/stop speaking", command=self.speaking_start)
        self.speaking_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=1)
        self.output_box = customtkinter.CTkTextbox(self, state = "disabled")
        self.output_box.grid(row=0, column=1, padx=20, pady=20, sticky="ew", columnspan=1, rowspan=2)
        # sleep(1)
        self.mode = 0
        self.var_check = 0
        self.callback_after = ""
        self.output_box.configure(state="normal")
        self.output_box.insert("1.0", "Speaking on.\n")
        if self.mode == 0:
            self.output_box.insert("2.0", "Listening from audio file.\n")
        if self.mode == 1:
            self.output_box.insert("2.0", "Listening from microphone.\n")
        self.output_box.configure(state="disabled")
        # self.speaking_start(self.speaking_button)
        # print(self.speaking_button._state)
        

    def speaking_start(self, *args):
        # print(self.var_check)
        # print(self.speaking_button.cget("state"))
        
        if self.var_check == 0:
            self.speaking_button.configure(command = self.speaking_stop)
            self.var_check = 1

        """params"""
        file = "public/go_forward.wav"
        # file = "public/stop.wav"
        """end"""
        query = ""
        r = sr.Recognizer()
        if self.mode == 0:
            with sr.AudioFile(file) as source:
                
                
                audio_data = r.record(source)
                # query = r.recognize_google(audio_data, language='en-US')
                query = r.recognize_google(audio_data)
                # query = "goo"
                print(query)
                self.output_box.configure(state="normal")
                self.output_box.insert("3.0", f"User said: {query}\n")
                self.output_box.configure(state="disabled")
        elif self.mode == 1:
            with sr.Microphone() as mic:
                
                r.adjust_for_ambient_noise(mic)
                
                self.output_box.configure(state="normal")
                try:
                    audio = r.listen(mic, timeout=5)
                    query = r.recognize_google(audio, language='en-US')
                    self.output_box.delete("3.0", "end")
                    self.output_box.insert("3.0", f"\nUser said: {query}\n")
                    
                except Exception:
                    self.output_box.delete("3.0", "end")
                    self.output_box.insert("3.0", "\nSay that again please.\n")

                self.output_box.configure(state="disabled")
                sleep(5)
        print(query)
        self.query_check(query)
        self.callback_after = self.speaking_button.after(5000, self.speaking_start)
        # print(self.callback_after)

        
    def query_check(self, *args):
        query=args[0]
        print(query)
        list_1 = ["go forward", "forward", "start", "move", "drive"]
        list_2 = ["stop", "break", "pause", "finish", "close", "end", "stay"]
        if query=="":
            pass
        elif query in list_1:
            forward.node_start(speed=0.5)
            print(query+" in list_1")
        elif query in list_2:
            stop.node_start()
            print(query+" in list_2")

        
    def speaking_stop(self):
        self.speaking_button.configure(command = self.speaking_start)
        self.var_check = 0
        self.speaking_button.after_cancel(self.callback_after)
        stop.node_start()
        self.output_box.configure(state="normal")
        self.output_box.insert("4.0", "Stopping.\n")
        self.output_box.configure(state="disabled")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("HMI")
        self.geometry("400x300")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0,1), weight=1)

        self.speed = 0.5
        self.forward_button = customtkinter.CTkButton(self, text="start", command=self.forward_button_callback, state="normal")
        self.forward_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=1)
        self.stop_button = customtkinter.CTkButton(self, text="stop", command=self.stop_button_callback)
        self.stop_button.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=1)
        self.speed_box = customtkinter.CTkEntry(self, placeholder_text=self.speed)
        self.speed_box.grid(row=0, column=1, padx=20, pady=20)
        self.speaking_switch = customtkinter.CTkButton(self, text="voice recognition", command=self.open_window)
        self.speaking_switch.grid(row=1, column=1, padx=20, pady=20, sticky="ew")
        self.top_level = None


    def open_window(self):
        if self.top_level is None or not self.top_level.winfo_exists():
            self.top_level = TopLevelWindow(self)
        else:
            self.top_level.focus()


    def forward_button_callback(self):
        self.forward_button.configure(state="normal")
        if len(self.speed_box.get())!=0:
            self.speed = self.speed_box.get()
        print("forward button pressed")
        print(self.speed)
        
        forward.node_start(self.speed)
        
        
    def stop_button_callback(self):
        print("stop button pressed")
        stop.node_start()

app = App()
app.mainloop()