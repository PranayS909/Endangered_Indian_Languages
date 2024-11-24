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
        "title": "Atong",
        "script_photo": "/mnt/data/India_Map.jpg",
        "description": "Atong language (Sino-Tibetan)-Atong is a Sino-Tibetan language spoken primarily by the Atong people in the Northeastern region of India, specifically in the state of Nagaland. Atong has a relatively small number of speakers, and it is considered an endangered language as it is facing gradual decline in favor of more widely spoken languages such as English and Nagamese.",
        "cultural_significance": "Atong language is a vital component of the Atong people’s cultural identity. It is used in traditional ceremonies, songs, and folklore that are important in the community’s rituals and everyday life. Festivals, rites of passage, and dance performances often involve storytelling and music in Atong, showcasing its cultural relevance.",
        "linguistic_significance": "Atong is a tonal language, where the meaning of words can change based on pitch or tone.It follows a subject-object-verb (SOV) sentence structure, which is typical of many Sino-Tibetan languages. Linguistic diversity within the Sino-Tibetan family: Atong contributes to the linguistic richness of the Sino-Tibetan family, with unique features compared to other languages in the region.",
    }

    open_button = tk.Button(root, text="Show Information on Atong Language", command=lambda: open_language_window(language_data))
    open_button.pack(expand=True, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()