import tkinter as tk
from PIL import Image, ImageTk

def main():
    def open_language_window(language_data):

        new_window = tk.Toplevel(root)
        new_window.title(language_data["title"])
        new_window.geometry("600x600")

        title_label = tk.Label(new_window, text=language_data["title"], font=("Arial", 20, "bold"))
        title_label.pack(pady=10)

        try:
            script_image = Image.open(language_data["script_photo"])
            script_image = script_image.resize((300, 200))
            photo = ImageTk.PhotoImage(script_image)
            script_label = tk.Label(new_window, image=photo)
            script_label.image = photo
            script_label.pack(pady=10)
        except FileNotFoundError:
            error_label = tk.Label(new_window, text="Script image not found.", font=("Arial", 12), fg="red")
            error_label.pack(pady=10)

        desc_label = tk.Label(new_window, text="Description:", font=("Arial", 16, "bold"))
        desc_label.pack(anchor="w", padx=20, pady=5)
        desc_text = tk.Label(new_window, text=language_data["description"], wraplength=500, justify="left", font=("Arial", 12))
        desc_text.pack(anchor="w", padx=20, pady=5)

        cultural_label = tk.Label(new_window, text="Cultural Significance:", font=("Arial", 16, "bold"))
        cultural_label.pack(anchor="w", padx=20, pady=5)
        cultural_text = tk.Label(new_window, text=language_data["cultural_significance"], wraplength=500, justify="left", font=("Arial", 12))
        cultural_text.pack(anchor="w", padx=20, pady=5)

        linguistic_label = tk.Label(new_window, text="Linguistic Significance:", font=("Arial", 16, "bold"))
        linguistic_label.pack(anchor="w", padx=20, pady=5)
        linguistic_text = tk.Label(new_window, text=language_data["linguistic_significance"], wraplength=500, justify="left", font=("Arial", 12))
        linguistic_text.pack(anchor="w", padx=20, pady=5)

    root = tk.Tk()
    root.title("Language Information")
    root.geometry("400x300")

    language_data = {
        "title": "Kolhati",
        "script_photo": "/mnt/data/India_Map.jpg",
        "description": "-Kolhati is a language spoken by the Kolhati people, who are mainly found in the Maharashtra state of India. It is part of the Indo-Aryan language family, which also includes languages like Hindi, Gujarati, and Marathi. Kolhati is not widely spoken anymore, and many Kolhati people now speak Marathi or Hindi in their daily lives, so this language is becoming less common.",
        "cultural_significance": "The Kolhati language is very important to the Kolhati community because it helps them keep their traditions, stories, and customs alive. In the past, they used the Kolhati language to tell folk tales, sing songs, and celebrate festivals, which passed down their culture to younger generations.",
        "linguistic_significance": "Kolhati has its own sounds and words that make it unique from languages like Marathi or Hindi, so it’s different in how it sounds and how sentences are put together. The language has a special grammar and word order, which makes it distinct from other languages spoken in the region. There is no special writing system for Kolhati, so it’s mostly shared through talking and listening.",
    }

    open_button = tk.Button(root, text="Show Information on Kolhati Language", command=lambda: open_language_window(language_data))
    open_button.pack(expand=True, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()