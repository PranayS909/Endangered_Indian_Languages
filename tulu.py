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
        "title": "Tulu",
        "script_photo": "/mnt/data/India_Map.jpg",
        "description": "Tulu is a language spoken by people in the southwestern part of India, especially in the state of Karnataka and Kerala. It's a part of the Dravidian language family, which includes other languages like Tamil, Telugu, and Kannada. Tulu is unique because it is not widely spoken outside of the region, but it has a rich history and is loved by the people who speak it. Many people who speak Tulu also speak Kannada or Malayalam.",
        "cultural_significance": "Tulu is important for the people who speak it because it helps them keep their cultural traditions alive. Tulu is used in many festivals, songs, and dances that are special to the Tulu-speaking community. For example, they have their own folk songs and plays, and Tulu is often used in religious ceremonies. Speaking Tulu connects people with their heritage and family history, and it helps them feel proud of their unique culture.",
        "linguistic_significance": "Linguistically, Tulu is interesting because it has its own set of sounds, words, and grammar. It uses a script called 'Tulu script' in some places, but many people write it in the Kannada script. Tulu has a special way of making sentences and is known for its unique words and expressions. Even though it’s not as widely spoken as other languages, Tulu is an important language for linguists to study because it helps them understand how languages in the Dravidian family have evolved.",
    }

    open_button = tk.Button(root, text="Show Information on Tulu Language", command=lambda: open_language_window(language_data))
    open_button.pack(expand=True, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()