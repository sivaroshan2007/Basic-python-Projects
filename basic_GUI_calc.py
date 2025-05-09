import tkinter as tk
from tkinter import *
window = tk.Tk()
window.title("SIMPLE CALCULATOR")
window.geometry("500x500")
numpad_frame = LabelFrame(window,text="number pad")
numpad_frame.pack(pady=100, fill=BOTH, expand=True)
value=IntVar

# to configrire the buttons 
numpad_frame.grid_propagate(False)  # Prevents widgets from auto-expanding
numpad_frame.grid_rowconfigure(0, weight=1)  
numpad_frame.grid_rowconfigure(1, weight=1)  # Set reasonable min size
numpad_frame.grid_columnconfigure(2, weight=1)
numpad_frame.grid_columnconfigure(3, weight=1)



############################## functions #####################################################
def button1():
    global value
    value = 1 

def button2():
    global value
    value = 2

def button3():
    global value
    value = 3

def multiplication():
    pass

def button4():
    global value
    value = 4

def button5():
    global value
    value = 5

def button6():
    global value
    value = 6

def button7():
    global value
    value = 7

def button8():
    global value
    value = 8

def button9():
    global value
    value = 9

def button0():
    global value
    value = 0

############################## functions #####################################################


############################### buttons ######################################################
b_1 = Button(numpad_frame, text="1",width=8,height=3,command=button1) 
b_1.grid(row=1, column=1,padx=30, sticky="nsew")

b_2 = Button(numpad_frame,text="2",width=8,height=3,command=button2)
b_2.grid(row=1, column=2,padx=30, sticky="nsew")

b_3 = Button(numpad_frame,text="3",width=8,height=3,command=button3)
b_3.grid(row=1, column=3,padx=30, sticky="nsew")

b_mul = Button(numpad_frame,text="X",width=8,height=3,command=multiplication)
b_mul.grid(row=1, column=4,padx=30, sticky="nsew")

b_4 = Button(numpad_frame,text="4",width=8,height=3,command=button4)
b_4.grid(row=2, column=1,padx=30,pady=10, sticky="nsew")

b_5 = Button(numpad_frame,text="5",width=8,height=3,command=button5)
b_5.grid(row=2, column=2,padx=30,pady=10, sticky="nsew")

b_6 = Button(numpad_frame,text="6",width=8,height=3,command=button6)
b_6.grid(row=2, column=3,padx=30,pady=10, sticky="nsew")

b_7 = Button(numpad_frame,text="7",width=8,height=3,command=button7)
b_7.grid(row=3, column=1,padx=30,pady=10, sticky="nsew")

b_8 = Button(numpad_frame,text="8",width=8,height=3,command=button8)
b_8.grid(row=3, column=2,padx=30,pady=10, sticky="nsew")

b_9 = Button(numpad_frame,text="9",width=8,height=3,command=button9)
b_9.grid(row=3, column=3,padx=30,pady=10, sticky="nsew")

b_0 = Button(numpad_frame,text="0",width=8,height=3,command=button0)
b_0.grid(row=4, column=2,padx=30,pady=10, sticky="nsew")
################################ buttons #####################################################


window.mainloop()