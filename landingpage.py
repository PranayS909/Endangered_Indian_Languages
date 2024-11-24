import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from kangri import main as kangri
from balti import main as balti
from pahari import main as pahari
from angika import main as angika
from asur import main as asur
from nihani import main as nihani
from kolhati import main as kolhati
from katkari import main as katkari
from atong import main as atong
from aimol import main as aimol
from kachari import main as kachari
from badaga import main as badaga
from tulu import main as tulu
from toda import main as toda
from gondi import main as gondi

def open_region_window(reg):
    if reg == "Northern":
        north(reg)
    elif reg == "Central":
        central(reg)
    elif reg == "Western":
        west(reg)
    elif reg == "Eastern":
        east(reg)
    elif reg == "Southern":
        south(reg)

def north(section):

    region_window = tk.Toplevel(window)
    region_window.title(f"{section} India")
    region_window.geometry("1000x1000")

    try:
        image = Image.open(r"C:\Users\prana\OneDrive\Desktop\Python Competition\Endangered_Indian_Languages\Endangered_Indian_Languages\abhishek-donda-JAoRJvvS4Jc-unsplash.jpg")
        image = image.resize((576, 432))
        photo = ImageTk.PhotoImage(image)
        img_label = tk.Label(region_window, image=photo)
        img_label.image = photo
        img_label.pack(pady=20)
    except FileNotFoundError:
        img_label = tk.Label(region_window, text="Image not found")
        img_label.pack(pady=20)

    label = tk.Label(region_window, text="Select an option:")
    label.pack(pady=5)

    options = ["Kangiri", "Balti", "Mahasu Pahari"]

    selected_option = tk.StringVar(value=options[0])

    dropdown = ttk.Combobox(region_window, textvariable=selected_option, values=options, state="readonly")
    dropdown.pack(pady=10)

    def handle_selection(event):
        if selected_option.get() == "Kangiri":
            kangri()
        elif selected_option.get() == "Balti":
            balti()
        elif selected_option.get() == "Mahasu Pahari":
            pahari()

    dropdown.bind("<<ComboboxSelected>>", handle_selection)

def central(section):

    region_window = tk.Toplevel(window)
    region_window.title(f"{section} India")
    region_window.geometry("1000x1000")

    try:
        image = Image.open(r"C:\Users\prana\OneDrive\Desktop\Python Competition\Endangered_Indian_Languages\Endangered_Indian_Languages\indian-travel-destination-beautiful-attractive.jpg")
        image = image.resize((525, 283))
        photo = ImageTk.PhotoImage(image)
        img_label = tk.Label(region_window, image=photo)
        img_label.image = photo
        img_label.pack(pady=20)
    except FileNotFoundError:
        img_label = tk.Label(region_window, text="Image not found")
        img_label.pack(pady=20)

    label = tk.Label(region_window, text="Select an option:")
    label.pack(pady=5)

    options = ["Angika", "Asur", "Gondi"]

    selected_option = tk.StringVar(value=options[0])

    dropdown = ttk.Combobox(region_window, textvariable=selected_option, values=options, state="readonly")
    dropdown.pack(pady=10)

    def handle_selection(event):
        if selected_option.get() == "Angika":
            angika()
        elif selected_option.get() == "Asur":
            asur()
        elif selected_option.get() == "Gondi":
            gondi()

    dropdown.bind("<<ComboboxSelected>>", handle_selection)

def west(section):

    region_window = tk.Toplevel(window)
    region_window.title(f"{section} India")
    region_window.geometry("1000x1000")

    try:
        image = Image.open(r"C:\Users\prana\OneDrive\Desktop\Python Competition\Endangered_Indian_Languages\Endangered_Indian_Languages\zoshua-colah-I66lOT6PNls-unsplash.jpg")
        image = image.resize((504, 283))
        photo = ImageTk.PhotoImage(image)
        img_label = tk.Label(region_window, image=photo)
        img_label.image = photo
        img_label.pack(pady=20)
    except FileNotFoundError:
        img_label = tk.Label(region_window, text="Image not found")
        img_label.pack(pady=20)

    label = tk.Label(region_window, text="Select an option:")
    label.pack(pady=5)

    options = ["Nihani", "Kolhati", "Katkari"]

    selected_option = tk.StringVar(value=options[0])

    dropdown = ttk.Combobox(region_window, textvariable=selected_option, values=options, state="readonly")
    dropdown.pack(pady=10)

    def handle_selection(event):
        if selected_option.get() == "Nihani":
            nihani()
        elif selected_option.get() == "Kolhati":
            kolhati()
        elif selected_option.get() == "Katkari":
            katkari()

    dropdown.bind("<<ComboboxSelected>>", handle_selection)

def east(section):

    region_window = tk.Toplevel(window)
    region_window.title(f"{section} India")
    region_window.geometry("1000x1000")

    try:
        image = Image.open(r"C:\Users\prana\OneDrive\Desktop\Python Competition\Endangered_Indian_Languages\Endangered_Indian_Languages\pratham-malviya-Hm59ASJxwJo-unsplash.jpg")
        image = image.resize((500, 416))
        photo = ImageTk.PhotoImage(image)
        img_label = tk.Label(region_window, image=photo)
        img_label.image = photo
        img_label.pack(pady=20)
    except FileNotFoundError:
        img_label = tk.Label(region_window, text="Image not found")
        img_label.pack(pady=20)

    label = tk.Label(region_window, text="Select an option:")
    label.pack(pady=5)

    options = ["Atong", "Aimol", "Kachari"]

    selected_option = tk.StringVar(value=options[0])

    dropdown = ttk.Combobox(region_window, textvariable=selected_option, values=options, state="readonly")
    dropdown.pack(pady=10)

    def handle_selection(event):
        if selected_option.get() == "Atong":
            atong()
        elif selected_option.get() == "Aimol":
            aimol()
        elif selected_option.get() == "Kachari":
            kachari()

    dropdown.bind("<<ComboboxSelected>>", handle_selection)

def south(section):

    region_window = tk.Toplevel(window)
    region_window.title(f"{section} India")
    region_window.geometry("1000x1000")

    try:
        image = Image.open(r"C:\Users\prana\OneDrive\Desktop\Python Competition\Endangered_Indian_Languages\Endangered_Indian_Languages\shawn-powar-9EHNzcwXTok-unsplash.jpg")
        image = image.resize((547, 365))
        photo = ImageTk.PhotoImage(image)
        img_label = tk.Label(region_window, image=photo)
        img_label.image = photo
        img_label.pack(pady=20)
    except FileNotFoundError:
        img_label = tk.Label(region_window, text="Image not found")
        img_label.pack(pady=20)

    label = tk.Label(region_window, text="Select an option:")
    label.pack(pady=5)

    options = ["Badaga", "Tulu", "Toda"]

    selected_option = tk.StringVar(value=options[0])

    dropdown = ttk.Combobox(region_window, textvariable=selected_option, values=options, state="readonly")
    dropdown.pack(pady=10)

    def handle_selection(event):
        if selected_option.get() == "Badaga":
            badaga()
        elif selected_option.get() == "Tulu":
            tulu()
        elif selected_option.get() == "Toda":
            toda()

    dropdown.bind("<<ComboboxSelected>>", handle_selection)


window = tk.Tk()
window.title("Reviving Endangered Languages of India")
window.geometry("1000x1000")
tk.Label(text="Reviving Endangered Languages of India", font = ("Arial", 25) ).pack()

try:
    image = Image.open(r"C:\Users\prana\OneDrive\Desktop\Python Competition\Endangered_Indian_Languages\Endangered_Indian_Languages\India_Map.jpg")
    image = image.resize((512, 600))
    photo = ImageTk.PhotoImage(image)
    img_label = tk.Label(window, image = photo)
    img_label.pack(pady=20)
except FileNotFoundError:
    img_label = tk.Label(window, text="Image not found")
    img_label.pack(pady=20)


regions = {
    "Northern": (345, 260),
    "Central": (440, 320),
    "Eastern": (540, 345),
    "Western": (360, 400),
    "Southern": (380, 500),
}

for region, position in regions.items():
    label = tk.Label(window, text=region, font=("Arial", 12), fg="blue", cursor="hand2")
    label.place(x=position[0], y=position[1])
    label.bind("<Button-1>", lambda e, r=region: open_region_window(r))

tk.Label(text="Select a region to know about its Endangered Languages", font = ("Arial", 12) ).pack()

window.mainloop()