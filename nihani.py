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
        "title": "Nihani",
        "script_photo": "/mnt/data/India_Map.jpg",
        "description": " Nihani-Nihali is a very old language spoken by a small group of people called the Nihal in parts of Madhya Pradesh and Maharashtra in India. It is different from many other languages spoken around it, so it is special and unique. Nihali doesn’t have many people who speak it anymore, and many of its speakers now use Hindi or Marathi instead. Because fewer people speak it, Nihali is considered an endangered language.",
        "cultural_significance": "The Nihali language is important to the Nihal people because it helps them stay connected to their history and traditions. In the past, they used Nihali to tell stories, sing songs, and share their customs. These helped teach younger generations about their culture and the way they lived. The language is also used in rituals and festivals, where it helps express their spiritual beliefs and celebrations.",
        "linguistic_significance": "Nihali has its own sounds and ways of speaking that make it different from Hindi and Marathi. It’s like a secret code for the people who speak it! The structure of the language (how words are put together in a sentence) is also different from other languages, and it has some special words that you won’t find in many other languages. There is no special writing system for Nihali, so it is mostly passed down by talking rather than writing.",
    }

    open_button = tk.Button(root, text="Show Information on Nihani Language", command=lambda: open_language_window(language_data))
    open_button.pack(expand=True, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()