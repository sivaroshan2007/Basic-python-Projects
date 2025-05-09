import tkinter as tk
from tkinter import *
window = tk.Tk()
window.title("SIMPLE CALCULATOR")
window.geometry("500x500")
numpad_frame = LabelFrame(window,text="number pad")
numpad_frame.pack()
window.mainloop()