import customtkinter
from scripts import forward, stop



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("HMI")
        self.geometry("400x150")
        self.grid_columnconfigure((0, 1), weight=1)

        self.speed = 0.5
        self.forward_button = customtkinter.CTkButton(self, text="start", command=self.forward_button_callback)
        self.forward_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=1)
        self.stop_button = customtkinter.CTkButton(self, text="stop", command=self.stop_button_callback)
        self.stop_button.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=1)
        self.speed_box = customtkinter.CTkEntry(self, placeholder_text=self.speed)
        self.speed_box.grid(row=0, column=1, padx=20, pady=20)

        
        

    def forward_button_callback(self):
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