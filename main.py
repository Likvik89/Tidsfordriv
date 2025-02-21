import tkinter as tk

# Function to switch between windows (frames)
def switch_frame(frame_to_show):
    frame_to_show.tkraise()

# Create the main window
root = tk.Tk()
root.title("Window Switcher")

# Create three frames
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)

# Create buttons in frame1
btn_to_frame2 = tk.Button(frame1, text="Go to Window 2", command=lambda: switch_frame(frame2))
btn_to_frame2.pack(pady=10)

btn_to_frame3 = tk.Button(frame1, text="Go to Window 3", command=lambda: switch_frame(frame3))
btn_to_frame3.pack(pady=10)

# Create buttons in frame2
btn_to_frame1 = tk.Button(frame2, text="Go to Window 1", command=lambda: switch_frame(frame1))
btn_to_frame1.pack(pady=10)

btn_to_frame3 = tk.Button(frame2, text="Go to Window 3", command=lambda: switch_frame(frame3))
btn_to_frame3.pack(pady=10)

# Create buttons in frame3
btn_to_frame1 = tk.Button(frame3, text="Go to Window 1", command=lambda: switch_frame(frame1))
btn_to_frame1.pack(pady=10)

btn_to_frame2 = tk.Button(frame3, text="Go to Window 2", command=lambda: switch_frame(frame2))
btn_to_frame2.pack(pady=10)

# Pack all frames
for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky="nsew")

# Show the first frame initially
switch_frame(frame1)

# Start the Tkinter event loop
root.mainloop()
