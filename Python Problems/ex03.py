from tkinter import Tk, Entry, Button, StringVar
from tokenize import String


class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False,False)

        self.equation=String

root= Tk()
root.mainloop()