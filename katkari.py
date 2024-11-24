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
        "title": "Katkari",
        "script_photo": "/mnt/data/India_Map.jpg",
        "description": "Katkari is a language spoken by the Katkari people, a tribal group mostly found in the western part of India, especially in Maharashtra and Gujarat. It is a part of the Dravidian language family, which includes languages like Tamil, Telugu, and Kannada. Although Katkari is an old and unique language, many Katkari people now speak Marathi or Hindi, so fewer people speak Katkari today. This makes the language endangered.",
        "cultural_significance": "The Katkari language is a key part of the Katkari people’s culture. It helps them tell stories, sing songs, and share traditions that have been passed down through generations. The language is used in rituals, festivals, and special ceremonies, helping the Katkari people connect with their history and their ancestors. By speaking Katkari, they can celebrate their identity and stay connected to their community and heritage.",
        "linguistic_significance": "Katkari has a unique way of speaking and sounds that are different from languages like Marathi or Hindi. This makes it special and distinct. It has its own grammar and way of putting words together to form sentences. It also has some special words that other languages don’t use. Katkari doesn’t have a specific writing system, so it’s mostly passed down through speaking and listening.",
    }

    open_button = tk.Button(root, text="Show Information on Katkari Language", command=lambda: open_language_window(language_data))
    open_button.pack(expand=True, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()