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
        "title": "Gondi",
        "script_photo": "/mnt/data/India_Map.jpg",
        "description": "Gondi is an Austroasiatic language spoken by the Gondi people, primarily in central India, including states like Madhya Pradesh, Chhattisgarh, Maharashtra, Telangana, and Andhra Pradesh.It is the mother tongue of the Gond tribe, one of the largest indigenous tribes in India.Gondi belongs to the Dravidian language family and is considered a minority language with several dialects.",
        "cultural_significance": "Gondi is a vehicle of oral traditions and plays an essential role in the cultural expression of the Gond community. It is used in rituals, storytelling, and folk music. The language is crucial for preserving the myths, legends, and oral history of the Gond tribe. The traditions and songs, often passed down through generations, are deeply rooted in Gondi.",
        "linguistic_significance": "Gondi exhibits typical features of Dravidian languages, such as retroflex consonants and agglutinative morphology, where suffixes are added to the root words. Though the language doesn’t have a standardized script, it has been written in the Devanagari script in some instances. Efforts are ongoing to develop a more accessible script and preserve the language.",
    }

    open_button = tk.Button(root, text="Show Information on Gondi Language", command=lambda: open_language_window(language_data))
    open_button.pack(expand=True, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()