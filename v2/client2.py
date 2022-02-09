import tkinter as tk
from tkinter import Entry, ttk
import func2
from tkinter.filedialog import askopenfilename
from sys import exit

class window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

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
    myHash=None
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Hash Algorithm?")
        label.pack(pady=10, padx=10)
        SHA256 = ttk.Button(self, text="SHA256",
                           command=lambda: func2.hashChoice("1"))
        SHA256.pack()

        SHA512 = ttk.Button(self, text="SHA512",
                            command=lambda: func2.hashChoice("2"))
        SHA512.pack()

        MD5 = ttk.Button(self, text="MD5",
                            command=lambda: func2.hashChoice("3"))
        MD5.pack()

class checkVal(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        valueBox = ttk.Entry(self)
        submitButton = ttk.Button(self, text="Submit", command=lambda: submit())
        valueBox.pack()
        submitButton.pack()

        def submit():
            pass
    

app = window()
app.mainloop()
    