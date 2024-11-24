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
        "title": "Toda",
        "script_photo": "/mnt/data/India_Map.jpg",
        "description": "Toda is a language spoken by the Toda people, who live in the mountains of southern India, mainly in the state of Tamil Nadu. The Toda language is part of the Dravidian language family, like Tamil and Telugu, but it's unique and spoken by only a small group of people. The Toda language is not spoken by many people outside their community, and there are fewer and fewer people who speak it today, which makes it a special and endangered language.",
        "cultural_significance": "The Toda language is very important for the Toda people because it helps them keep their traditions alive. They use the language for storytelling, singing, and during religious ceremonies. The Toda people have unique customs, and their language helps pass down old stories, knowledge about nature, and even rules for how to live in their community. The language is also tied to their special way of life in the mountains, where they raise cattle and live in small villages. Speaking Toda helps people stay connected to their history and culture.",
        "linguistic_significance": "Linguistically, Toda is interesting because it has some special sounds and words that make it different from many other languages. It has a unique grammar and uses certain vowel sounds and consonants that aren’t found in many other languages, even those in the Dravidian family. Toda is also an oral language, meaning that it is mostly spoken and not written down, which makes it harder for people outside the community to learn it. Linguists study Toda to understand more about how languages change and how different languages are connected to each other.",
    }

    open_button = tk.Button(root, text="Show Information on Toda Language", command=lambda: open_language_window(language_data))
    open_button.pack(expand=True, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()