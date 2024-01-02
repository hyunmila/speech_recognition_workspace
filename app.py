import customtkinter
from scripts import forward, stop
from src.reco import takeCommand


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("HMI")
        self.geometry("400x400")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)

        self.speed = 0.5
        self.forward_button = customtkinter.CTkButton(self, text="start", command=self.forward_button_callback, state="normal")
        self.forward_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=1)
        self.stop_button = customtkinter.CTkButton(self, text="stop", command=self.stop_button_callback)
        self.stop_button.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=1)
        self.speed_box = customtkinter.CTkEntry(self, placeholder_text=self.speed)
        self.speed_box.grid(row=0, column=1, padx=20, pady=20)
        self.speaking_switch_on = customtkinter.CTkButton(self, text="voice recognition", command=self.switch_on_callback)
        # switch_var = customtkinter.StringVar(value="off")
        # self.speaking_switch = customtkinter.CTkSwitch(self, text="voice recognition", command=self.speaking_switch_callback, variable=switch_var, onvalue="on", offvalue="off")
        self.speaking_switch_on.grid(row=1, column=1, padx=20, pady=20, sticky="ew")
        self.speaking_switch_off = customtkinter.CTkButton(self, text="voice recognition", command=self.switch_off_callback)
        self.speaking_switch_off.grid(row=2, column=1, padx=20, pady=20, sticky="ew")
        self.button = customtkinter.CTkSegmentedButton(self, values=["on", "off"], command=self.test_button)
        self.button.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        self.button.set(value="off")
        
    def test_button(self, value):
        
        print("ass")
        if value=="on":
            query = takeCommand().lower()
            print(query)
        else:
            print("stopping voice recognition")


    def switch_on_callback(self):
        self.speaking_start("on")
    def switch_off_callback(self):
        self.speaking_start("off")
        # if self.speaking_switch_on.get() == "on":
        # if param=="on":
        #     query = takeCommand().lower()
        #     print(query)
        # else:
        #     print("stopping voice recognition")
            # self.forward_button.invoke()
    


    def speaking_start(self, param):
        if param=="on":
            query = takeCommand().lower()
            print(query)
        else:
            print("stopping voice recognition")


    def forward_button_callback(self):
        self.forward_button.configure(state="normal")
        if len(self.speed_box.get())!=0:
            self.speed = self.speed_box.get()
        print("forward button pressed")
        print(self.speed)
        
        # forward.node_start(self.speed)
        
        
    def stop_button_callback(self):
        print("stop button pressed")
        # stop.node_start()

app = App()
app.mainloop()