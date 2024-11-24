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
        "title": "Kachari",
        "script_photo": "/mnt/data/India_Map.jpg",
        "description": "-Kachari is a Bodo-Garo language spoken by the Kachari people, an indigenous group primarily located in Assam and some parts of Nagaland, Meghalaya, and West Bengal in India.Kachari is primarily an oral language, and while there is some use of the Bengali script for writing, efforts to standardize the language and preserve it are ongoing.",
        "cultural_significance": "Kachari language is deeply tied to the identity of the Kachari people. It is a medium for their oral traditions, including myths, folklore, and rituals, which have been passed down through generations.Kachari traditions: Through its language, the Kachari people maintain their traditional worldview, values, and a close connection to their ancestors. It serves as a tool for preserving historical narratives, reinforcing the community’s unique cultural practices.",
        "linguistic_significance": "Kachari exhibits features common to many Bodo-Garo languages, including a subject-object-verb (SOV) word order. The language is tonal, where variations in pitch can change the meaning of words, making it phonetically rich and distinct from non-tonal languages in the region. Morphologically, Kachari uses agglutination, adding affixes to root words to express grammatical relations, which is a characteristic feature of many Sino-Tibetan languages.",
    }

    open_button = tk.Button(root, text="Show Information on Kachari Language", command=lambda: open_language_window(language_data))
    open_button.pack(expand=True, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()