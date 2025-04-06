import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors
import random

def get_primary_monitor():
    for monitor in get_monitors():
        if monitor.is_primary:
            return monitor

def get_center(width, height):
    monitor = get_primary_monitor()
    x = (monitor.width - width) // 2
    y = (monitor.height - height) // 2
    return x, y

def clicked_yes():  
    for widget in window.winfo_children():  
        widget.destroy()

    label = ttk.Label(window, text="I knew it! :D", font="Calibri 25 bold")
    label.pack(expand=True)

def generate_random_cords():
    x_cords = random.randint(5, 230)
    y_cords = random.randint(5, 265)
    return x_cords, y_cords

def random_position(event=None):
    mouse_x = event.x_root - window.winfo_rootx()
    mouse_y = event.y_root - window.winfo_rooty()

    button_width = no_button.winfo_width()
    button_height = no_button.winfo_height()

    margin = 20

    x_cords, y_cords = generate_random_cords()

    while (x_cords < mouse_x + margin and x_cords + button_width > mouse_x - margin) and \
          (y_cords < mouse_y + margin and y_cords + button_height > mouse_y - margin):
        x_cords, y_cords = generate_random_cords()

    no_button.place(x=x_cords, y=y_cords)

window = tk.Tk()
window.title("")
window.resizable(False, False)
width=300
height=300

x, y = get_center(width, height)
window.geometry(f"{width}x{height}+{x}+{y}")

label = ttk.Label(window, text="Are u dumb?", font="Calibri 25 bold")
label.pack(pady=40)

button_style = ttk.Style()
button_style.configure("secondary.TButton", font="Calibri 12", width=7)

yes_button = ttk.Button(window, text="Yes", style="secondary.TButton", command=clicked_yes)
no_button = ttk.Button(window, text="No", style="secondary.TButton", command=lambda: no_button.destroy())

yes_button.place(x=64, y=194)
no_button.place(x=170, y=194)

no_button.bind("<Enter>", random_position)
window.mainloop()
