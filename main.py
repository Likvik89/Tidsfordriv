import tkinter as tk

# Function to switch between windows (frames)
def switch_frame(frame_to_show):
    frame_to_show.tkraise()

# Create the main window
root = tk.Tk()
root.title("Window Switcher")

# Create three frames (Start, Morse, Caesar)
start_frame = tk.Frame(root)
morse_frame = tk.Frame(root)
caesar_frame = tk.Frame(root)

# Create buttons in the start frame
btn_to_morse = tk.Button(start_frame, text="Go to Morse", command=lambda: switch_frame(morse_frame))
btn_to_morse.pack(pady=10)

btn_to_caesar = tk.Button(start_frame, text="Go to Caesar", command=lambda: switch_frame(caesar_frame))
btn_to_caesar.pack(pady=10)

# Create buttons in the morse frame
btn_to_start = tk.Button(morse_frame, text="Go to Start", command=lambda: switch_frame(start_frame))
btn_to_start.pack(pady=10)

btn_to_caesar = tk.Button(morse_frame, text="Go to Caesar", command=lambda: switch_frame(caesar_frame))
btn_to_caesar.pack(pady=10)

# Create buttons in the caesar frame
btn_to_start = tk.Button(caesar_frame, text="Go to Start", command=lambda: switch_frame(start_frame))
btn_to_start.pack(pady=10)

btn_to_morse = tk.Button(caesar_frame, text="Go to Morse", command=lambda: switch_frame(morse_frame))
btn_to_morse.pack(pady=10)

# Pack all frames
for frame in (start_frame, morse_frame, caesar_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# Show the start frame initially
switch_frame(start_frame)

# Start the Tkinter event loop
root.mainloop()
