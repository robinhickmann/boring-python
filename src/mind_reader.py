import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors

def get_primary_monitor():
    for monitor in get_monitors():
        if monitor.is_primary:
            return monitor

def get_center(width, height):
    monitor = get_primary_monitor()
    x = (monitor.width - width) // 2
    y = (monitor.height - height) // 2
    return x, y

def validate_input(P):
  return P == "" or str.isdigit(P) and int(P) >= 1 and int(P) <= 10

def read_mind():
    if entry.get() == "":
        return
    if result_window is not None:
        result_window.destroy()
    button.config(state=tk.DISABLED)

    window = tk.Tk()
    window.title("Reading your mind")
    window.resizable(False, False)
    window.geometry(f"{width}x{140}+{x}+{y}")

    label = ttk.Label(window, text=progress_text[0])
    label.pack(pady=40)

    bar = ttk.Progressbar(window, length=250, mode="determinate")
    bar.pack(pady=5)
    
    update_progress(window, bar, label)

def update_progress(window, bar, label):
    bar['value'] += 1

    if bar['value'] < 100:
        if bar['value'] % 25 == 0:
                label.config(text=progress_text[int(bar['value'] // 25)])
        
        window.after(60, update_progress, window, bar, label)
    else:
        window.destroy()
        button.config(state=tk.NORMAL)
        display_result()

def display_result():
    window = tk.Tk()
    window.title("Mind Reader")
    window.resizable(False, False)
    window.geometry(f"{270}x{90}+{x}+{y}")

    label = ttk.Label(window, text="Your thinking of the number " + entry.get() + ".")
    label.pack(pady=30)

    global result_window
    result_window = window

result_window = None
window = tk.Tk()
window.title("Mind Reader")
window.resizable(False, False)
width = 300
height = 200
progress_text = [
    "Analyzing brainwaves...",
    "Scanning memories...",
    "Calculating probabilities...",
    "Decoding thoughts..."
]

x, y = get_center(width, height)
window.geometry(f"{width}x{height}+{x}+{y}")

label = ttk.Label(window, text="Think of a number between 1 and 10:")
label.pack(pady=40)

validate_cmd = window.register(validate_input)

entry = ttk.Entry(window, validate="all", validatecommand=(validate_cmd, '%P'))
entry.pack(pady=5)

button = ttk.Button(window, text="Read my mind", command=read_mind)
button.pack(pady=20)

window.mainloop()
