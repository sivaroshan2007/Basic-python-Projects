import tkinter as tk
from tkinter import *
from tkinter import ttk 

window = tk.Tk()
window.title("SIMPLE CALCULATOR")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight() 

window.geometry(f"{screen_width}x{screen_height}")


txtpadframe = Frame(window,height=50,width=600)
txtpadframe.pack(fill=BOTH,expand=True)

numpad_frame = LabelFrame(window,text="number pad")
numpad_frame.pack(pady=(5,20),padx=(20,350),anchor='ne',expand=True,fill='both')
#numpad_frame.config(width=30, height=800)

for i in range(6):  # Assuming 6 rows
    numpad_frame.grid_rowconfigure(i, weight=2)
for j in range(5):  # Assuming 4 columns
    numpad_frame.grid_columnconfigure(j, weight=2)



history_frame = LabelFrame(window,text='History',height=600)
history_frame.pack(padx=(20,20),pady=(10,10),anchor='ne')
history_frame.config(height=600,width=30)


value=IntVar()

# to configrire the buttons 
numpad_frame.grid_propagate(False)  # Prevents widgets from auto-expanding
numpad_frame.grid_rowconfigure(0, weight=1)  
numpad_frame.grid_rowconfigure(0, weight=1)  # Set reasonable min size
numpad_frame.grid_columnconfigure(0, weight=1)
numpad_frame.grid_columnconfigure(0, weight=1)



############################## functions #####################################################
def button1():
    global value
    value.set(1)
    txtbox.insert(10, str(value.get()))

def button2():
    global value
    value.set(2)
    txtbox.insert(10, str(value.get()))
    
def button3():
    global value
    value.set(3)
    txtbox.insert(10, str(value.get()))

def multiplication():       #functions involving logics#
    pass

def divison():
    pass

def addition():
    pass

def subraction():
    pass

def clear():
    pass

def clearall():
    pass

def sqroot():
    pass

def square():
    pass

def equalto():
    pass
                         #functions involving logics#
def button4():
    global value
    value.set(4)
    txtbox.insert(10, str(value.get()))

def button5():
    global value
    value.set(5)
    txtbox.insert(10, str(value.get()))

def button6():
    global value
    value.set(6)
    txtbox.insert(10, str(value.get()))

def button7():
    global value
    value.set(7)
    txtbox.insert(10, str(value.get()))

def button8():
    global value
    value.set(8)
    txtbox.insert(10, str(value.get()))

def button9():
    global value
    value.set(9)
    txtbox.insert(10, str(value.get()))

def button0():
    global value
    value.set(0)
    txtbox.insert(10, str(value.get()))
############################## functions #####################################################


############################### buttons ######################################################
b_1 = Button(numpad_frame, text="1",width=8,height=3,command=button1) 
b_1.grid(row=1, column=1,padx=30,sticky="nsew")

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

b_6 = Button(numpad_frame,text="/",width=8,height=3,command=divison)
b_6.grid(row=2, column=4,padx=30,pady=10, sticky="nsew")

b_7 = Button(numpad_frame,text="7",width=8,height=3,command=button7)
b_7.grid(row=3, column=1,padx=30,pady=10, sticky="nsew")

b_8 = Button(numpad_frame,text="8",width=8,height=3,command=button8)
b_8.grid(row=3, column=2,padx=30,pady=10, sticky="nsew")

b_9 = Button(numpad_frame,text="9",width=8,height=3,command=button9)
b_9.grid(row=3, column=3,padx=30,pady=10, sticky="nsew")

b_9 = Button(numpad_frame,text="+",width=8,height=3,command=addition)
b_9.grid(row=3, column=4,padx=30,pady=10, sticky="nsew")


b_0 = Button(numpad_frame,text="0",width=8,height=3,command=button0)
b_0.grid(row=4, column=2,padx=30,pady=10, sticky="nsew")


b_clear = Button(numpad_frame,text="C",width=8,height=3,command=clear)
b_clear.grid(row=4, column=3,padx=30,pady=10, sticky="nsew")

b_clearall = Button(numpad_frame,text="CE",width=8,height=3,command=clearall)
b_clearall.grid(row=4, column=1,padx=30,pady=10, sticky="nsew")

b_sub = Button(numpad_frame,text="-",width=8,height=3,command=subraction)
b_sub.grid(row=4, column=4,padx=30,pady=10, sticky="nsew")

b_sqroot = Button(numpad_frame,text="x^1/2",width=8,height=3,command=sqroot)
b_sqroot.grid(row=5, column=1,padx=30,pady=10, sticky="nsew")

b_square = Button(numpad_frame,text="x^2",width=8,height=3,command=square)
b_square.grid(row=5, column=2,padx=30,pady=10, sticky="nsew")

b_dot = Button(numpad_frame,text=".",width=8,height=3,command=subraction)
b_dot.grid(row=5, column=3,padx=30,pady=10, sticky="nsew")

b_equalto = Button(numpad_frame,text="=",width=8,height=3,command=equalto)
b_equalto.grid(row=5, column=4,padx=30,pady=10, sticky="nsew")
################################ buttons #####################################################


############################## Entry box #####################################################
txtbox = Entry(txtpadframe,width=100,font=('times',50))
txtbox.pack(ipady=10)

history_box = ttk.Treeview(history_frame,height=300)
history_box.pack(ipady=600,padx=(20,20),pady=(10,10),anchor='ne')
############################## Entry box #####################################################

window.mainloop()
