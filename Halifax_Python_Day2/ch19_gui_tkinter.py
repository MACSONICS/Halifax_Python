#pip install tkinter
import tkinter as tk

window = tk.Tk()
window.mainloop()

from tkinter import *

window = Tk()

greeting = Label(window, text="Hello, Tkinter").place(x=70, y=90)
window.mainloop()

from tkinter import *

window = Tk()

label = Label(window, 
              text="Hello, Tkinter",
              foreground="white", # Set the text color to white
              background="black"  # Set the background color to black            
              ).place(x=70, y=90)

window.mainloop()

from tkinter import *

window = Tk()

button = Button(window,
                text="Click me!",
                width=25,
                height=5,
                bg="purple",
                fg="yellow").place(x=10, y=50)

window.mainloop()

from tkinter import *
from tkinter import ttk

# Create an instance of Tkinter frame
win = Tk()

# Set the title of the Tkinter frame
win.title("Python tkinter")

# Set the geometry of Tkinter frame
win.geometry("750x250")

def display_text():
    global entry
    string = entry.get()
    label.configure(text=string)

# Initialize a Label to display the User Input
label = Label(win, text="", font=("Courier 22 bold"))
label.pack()

# Create an Entry widget to accept User Input
entry = Entry(win, width=40)
entry.focus_set()
entry.pack()

# Create a Button to validate Entry Widget
ttk.Button(win, text="Okay", width=20, command=display_text).pack(pady=20)

win.mainloop()

from tkinter import *

# Create an instance of tkinter window or frame
win = Tk()
win.geometry("700x300")

# Creating a text box widget
my_text_box = Text(win, height=5, width=40)
my_text_box.pack()

def get_input():
    value = my_text_box.get("1.0", "end-1c")
    # Ensure this captures from the beginning to just before the last character (which is new line character in tkinter Text widgets)
    print(value)# This prints to the console, not to the tkinter window



# Create a button for Comment
comment = Button(win, height=3, width=10, text="Click Here....", command=get_input)
comment.pack()

win.mainloop()

from tkinter import *
win = Tk()

win.geometry("300x150")

w = Label(win, text="The main label", font="50")
w.pack()

frame = Frame(win)
frame.pack()

bottomframe = Frame(win)
bottomframe.pack(side=BOTTOM)

b1_button = Button(frame, text="Frame 1 on top", fg="red")
b1_button.pack(side=TOP)

b2_button = Button(frame, text="Frame 2 on left", fg="purple")
b2_button.pack(side=LEFT)

b3_button = Button(frame, text="Frame 3 on right", fg="brown")
b3_button.pack(side=RIGHT)

b4_button = Button(bottomframe, text="Frame 4 on bottom", fg="green")
b4_button.pack(side=BOTTOM)

win.mainloop()
'''
Each Frame is placed at the topmost available position. Therefore, the purple 
Frame is placed at the top of the window. Then the indigo
Frame is placed just below the purple one and the blue
Frame just below the indigo one.
There are three invisible parcels, each containing one of the three Frame
widgets. Each parcel is as wide as the window and as tall as the
Frame that it contains. Because no anchor point was specified when .pack()
was called for each Frame, they're all centered inside of their parcels. Tha,s why each Frame is centered in the window.

'''
import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="purple")
frame1.pack()

frame2 = tk.Frame(master=window, width=50, height=50, bg="indigo")
frame2.pack()

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack()

window.mainloop()


import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, height=100, bg="purple")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=window, height=50, bg="indigo")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=window, height=25, bg="blue")
frame3.pack(fill=tk.X)

window.mainloop()

import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=200, height=100, bg="purple")
frame1.pack(fill=tk.Y, side=tk.LEFT)

frame2 = tk.Frame(master=window, width=100, bg="indigo")
frame2.pack(fill=tk.Y, side=tk.LEFT)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.Y, side=tk.LEFT)

window.mainloop()

import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="green")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="I'm at (20, 25)", bg="purple")
label2.place(x=20, y=25)

label3 = tk.Label(master=frame, text="I'm at (50, 50)", bg="orange")
label3.place(x=50, y=50)

window.mainloop()

import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i} Column {j}")
        label.pack()

window.mainloop()
