import tkinter as tk
from tkinter import Entry, ttk
import functions
from tkinter.filedialog import askopenfilename
from sys import exit

class window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.iconbitmap(self, default='walnutfolder/walnut.ico')
        #tk.Tk.wm_title(self, "WalnutCord")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in(StartPage,checkVal):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Walnut")
        label.pack(pady=10, padx=10)
        
        def Choice(choice):
            global hash
            file = askopenfilename()
            if file:
                hash = functions.hashchoice(choice, file)
                controller.show_frame(checkVal)
            else:
                exit()
            
        SHA256 = ttk.Button(self, text="SHA256",
                           command=lambda: Choice("1"))
        SHA256.pack()

        SHA512 = ttk.Button(self, text="SHA512",
                            command=lambda: Choice("2"))
        SHA512.pack()

        MD5 = ttk.Button(self, text="MD5",
                            command=lambda: Choice("3"))
        MD5.pack()

class checkVal(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        valueBox = ttk.Entry(self)
        submitButton = ttk.Button(self, text="Submit", command=lambda: submit())
        valueBox.pack()
        submitButton.pack()

        def submit():
            global hash
            matching=ttk.Label(self, text="")
            print(hash.hexdigest())
            print(valueBox.get())
            if valueBox.get() == (hash.hexdigest()):
                matching.config(text="Values match")
                matching.pack_forget()


            else:
                matching.config(text="Values do not match")
                matching.pack()
    



app = window()
app.mainloop()