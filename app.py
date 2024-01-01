import customtkinter
from scripts import forward, stop
# def button_callback():
#     print("button pressed")

# app = customtkinter.CTk()
# app.title("HMI")
# app.geometry("400x150")

# forward_button = customtkinter.CTkButton(app, text="go forward", command=button_callback)
# forward_button.grid(row=0, column=0, padx=20, pady=20)

# stop_button = customtkinter.CTkButton(app, text="stop", command=button_callback)
# stop_button.grid(row=1, column=0, padx=20, pady=20)

# app.mainloop()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("HMI")
        self.geometry("400x150")
        self.grid_columnconfigure((0, 1), weight=1)

        self.forward_button = customtkinter.CTkButton(self, text="go forward", command=self.forward_button_callback)
        self.forward_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=1)
        self.stop_button = customtkinter.CTkButton(self, text="stop", command=self.stop_button_callback)
        self.stop_button.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=1)
        
    def forward_button_callback(self):
        print("forward button pressed")
        forward.node_start()
        
        
    def stop_button_callback(self):
        print("stop button pressed")
        stop.node_start()

app = App()
app.mainloop()