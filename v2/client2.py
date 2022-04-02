import tkinter as tk
from tkinter import ttk
import hash_utils


class Window(tk.Tk):

    def __init__(self, *args, **kwargs):

        super(Window, self).__init__(*args, **kwargs)

        self.object = None

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for f in (StartPage, CheckVal):
            frame = f(container, self) if f == StartPage else f(container)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        def choice(option):
            my_hash = hash_utils.hash_choice(option)
            parent.object = hash_utils.file_choice(my_hash)
            controller.show_frame(CheckVal)

        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Hash Algorithm?")
        label.pack(pady=10, padx=10)
        sha256 = ttk.Button(self, text="SHA256", command=lambda: choice("1"))
        sha256.pack()

        sha512 = ttk.Button(self, text="SHA512", command=lambda: choice("2"))
        sha512.pack()

        md5 = ttk.Button(self, text="MD5", command=lambda: choice("3"))
        md5.pack()


class CheckVal(tk.Frame):

    def __init__(self, parent):

        super(CheckVal, self).__init__(parent)

        value_box = ttk.Entry(self)
        submit_button = ttk.Button(self, text="Submit", command=lambda: submit())

        matching = ttk.Label(self, text="")

        value_box.pack()
        submit_button.pack()

        def submit():

            if hash_utils.compare(parent.object, value_box.get()):
                matching.pack_forget()
                matching.configure(text="The values match")
                matching.pack()
            else:
                matching.pack_forget()
                matching.configure(text="The values do not match")
                matching.pack()


app = Window()
app.mainloop()
