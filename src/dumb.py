import tkinter as tk
from tkinter import ttk
import random

def get_center(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    return x, y

def clicked_yes():  
    for widget in window.winfo_children():  
        widget.destroy()

    label = ttk.Label(window, text="I knew it! :D", font="Calibri 25 bold")
    label.pack(expand=True)

def random_position(event = None):
    x_cords, y_cords = random.randint(5, 230), random.randint(5, 265)
    no_button.place(x=x_cords, y=y_cords)

window = tk.Tk()
window.title("")
window.resizable(False, False)
width=300
height=300

x, y = get_center(window, width, height)
window.geometry(f"{width}x{height}+{x}+{y}")

label = ttk.Label(window, text="Are u dumb?", font="Calibri 25 bold")
label.pack(pady=40)

button_style = ttk.Style()
button_style.configure("secondary.TButton", font="Calibri 12", width=7)

yes_button = ttk.Button(window, text="Yes", style="secondary.TButton", command=clicked_yes)
no_button = ttk.Button(window, text="No", style="secondary.TButton", command=random_position)

yes_button.place(x=64, y=194)
no_button.place(x=170, y=194)

no_button.bind("<Enter>", random_position)
window.mainloop()
