import tkinter as tk
from tkinter import *
from tkinter import ttk

def show_screen2():
    # Hide the first screen
    screen1.pack_forget()

    # Create the second screen (screen2)
    screen2.pack()

def show_screen1():
    # Hide the second screen
    screen2.pack_forget()

    # Create the first screen (screen1)
    screen1.pack()

# Set up the main window
root = tk.Tk()
root.title("Screen Switcher")

# First screen setup
screen1 = tk.Frame(root)
button1 = tk.Button(screen1, text="Go to Screen 2", command=show_screen2)
button1.pack(padx=20, pady=20)

# Second screen setup
screen2 = tk.Frame(root)
button2 = tk.Button(screen2, text="Go back to Screen 1", command=show_screen1)
button2.pack(padx=20, pady=20)

# Start with the first screen visible
screen1.pack()

# Run the main event loop
root.mainloop()
