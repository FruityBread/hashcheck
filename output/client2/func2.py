import sys
import hashlib
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import ttk

def hashChoice(choice):
    if choice =="1":
        type = ("SHA256")
        myHash = hashlib.sha256()
    elif choice =="2":
        type = ("SHA512")
        myHash = hashlib.sha512()
    elif choice=="3":
        type = ("MD5")
        myHash = hashlib.md5()
    else:
        print("Please enter a valid option.")
        hashChoice()
    return myHash

def fileChoice(myHash):
    file = askopenfilename()
    if file:
        with open((file), 'rb') as f:
            while True:
                data = f.read(65536)
                if not data:
                    myObj = hashObj(myHash,None)
                    print(myObj.myHash.hexdigest())
                    return myObj
                    print(myObj.myHash.hexdigest())

                    break
                myHash.update(data)
                

    else:
        exit()


class hashObj():
    def __init__(self, myHash, realHash):
        if myHash:
            self.myHash=myHash
        if realHash:
            self.realHash=realHash


def compare(myObj):
    if myObj.myHash.hexdigest() == myObj.realHash:
        return True
    else:
        return False




