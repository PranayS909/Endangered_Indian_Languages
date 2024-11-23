import tkinter as tk
from tkinter import messagebox

# Function to handle click events
def on_map_click(event):
    x, y = event.x, event.y
    # Check which region is clicked based on coordinates
    if 100 <= x <= 200 and 50 <= y <= 150:
        messagebox.showinfo("Region Clicked", "You clicked Northern Region!")
    elif 200 <= x <= 300 and 150 <= y <= 250:
        messagebox.showinfo("Region Clicked", "You clicked Western Region!")
    elif 300 <= x <= 400 and 200 <= y <= 300:
        messagebox.showinfo("Region Clicked", "You clicked Central Region!")
    elif 400 <= x <= 500 and 300 <= y <= 400:
        messagebox.showinfo("Region Clicked", "You clicked Southern Region!")
    elif 500 <= x <= 600 and 100 <= y <= 200:
        messagebox.showinfo("Region Clicked", "You clicked Eastern Region!")
    else:
        messagebox.showinfo("No Region", "Click inside the map regions.")

# Main Application
root = tk.Tk()
root.title("Clickable India Map")

# Load Map Image
canvas = tk.Canvas(root, width=700, height=500)
canvas.pack()

# Insert the Map Image (replace 'india_map.png' with your image file)
map_image = tk.PhotoImage(file="C:\Users\user\Documents\GitHub\Endangered_Indian_Languages\jpg2png.zip")
canvas.create_image(0, 0, anchor=tk.NW, image=map_image)

# Bind click event to the map
canvas.bind("<Button-1>", on_map_click)

# Run the application
root.mainloop()
