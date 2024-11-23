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
        "title": "Angika",
        "script_photo": "/mnt/data/India_Map.jpg",
        "description": "The Angika language is an Indo-Aryan language spoken in the central regions of India parts of Bihar, Jharkhand. It is primarily associated with the Anga region, which includes districts like Bhagalpur, Munger, and Banka. Angika has around 10–15 million speakers and is closely related to Maithili, Magahi, and Bhojpuri.Though historically significant as the language of the ancient Anga kingdom, Angika currently faces challenges in its recognition as a distinct language. It is often classified as a dialect of Maithili or Hindi in official contexts. Despite this, it remains vibrant in oral traditions and local culture.The language, though overshadowed by Hindi in recent years, remains an integral part of the heritage and identity of its speakers, contributing to India’s linguistic diversity.",
        "cultural_significance": "Historical Legacy: Angika is associated with the ancient Anga kingdom, mentioned in Hindu epics like the Mahabharata. The language reflects the traditions and historical narratives of this region.",
        "linguistic_significance": "Angika has preserved a rich oral tradition, with its folk literature providing insights into the linguistic and cultural history of eastern India.",
    }

    open_button = tk.Button(root, text="Show Information on Angika Language", command=lambda: open_language_window(language_data))
    open_button.pack(expand=True, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()