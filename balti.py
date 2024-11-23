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
    root.title("Balti")
    root.geometry("400x300")

    language_data = {
        "title": "Sanskrit",
        "script_photo": "/mnt/data/India_Map.jpg",
        "description": "The Balti language is a member of the Tibetic branch of the Sino-Tibetan language family and is primarily spoken in the far norther regions of India in parts of  Ladakh, India. With approximately 400,000 speakers, it is closely related to Classical Tibetan and shares similarities with Ladakhi and other Tibetan dialects.",
        "cultural_significance": "The phonetics of the Balti language features a set of consonant sounds including bilabial plosives like /p/, /ph/, and /b/, a nasal /m/, a glide /w/, and a distinct set of glottal plosives like /q/, /x/, and /g/, with the notable characteristic of having a separate phoneme for the aspirated ph sound, unlike English; it also has a range of vowel sounds with variations in articulation depending on the speaker and dialect.",
        "linguistic_significance": "It preserves the ethnic roots and traditions of the region, reflecting its rich history and social values.",
    }

    open_button = tk.Button(root, text="Show Information on Balti Language", command=lambda: open_language_window(language_data))
    open_button.pack(expand=True, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()