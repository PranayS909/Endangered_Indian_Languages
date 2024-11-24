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
        "title": "Aimol",
        "script_photo": "/mnt/data/India_Map.jpg",
        "description": "Aimol is a Tibeto-Burman language spoken primarily by the Aimol people in the Northeastern region of India, particularly in the Manipur state, and some parts of Myanmar.Aimol is a minority language with a relatively small number of speakers, making it vulnerable to extinction as younger generations shift to dominant regional languages like Manipuri and Hindi.The language does not have a standardized script, but it is primarily spoken, with efforts to document it in the Roman script and Manipuri script for academic purposes.",
        "cultural_significance": "The Aimol language is a key part of the Aimol people’s cultural identity. It is used in rituals, songs, folktales, and oral traditions, passing down the community’s history, values, and customs. Language plays an important role in community cohesion, as it is used in traditional ceremonies and festivals that celebrate the Aimol people’s connection to their land, ancestors, and spiritual beliefs.",
        "linguistic_significance": "Aimol follows a subject-object-verb (SOV) word order, typical of many Tibeto-Burman languages. It is a tonal language, meaning that pitch or tone changes can alter the meaning of words, adding complexity to its phonetic structure. The language has distinct phonological characteristics, including sounds that may not exist in neighboring languages like Manipuri or other Tibeto-Burman languages.",
    }

    open_button = tk.Button(root, text="Show Information on Aimol Language", command=lambda: open_language_window(language_data))
    open_button.pack(expand=True, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()