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
        "title": "Mahasu Pahari",
        "script_photo": "/mnt/data/India_Map.jpg",
        "description": "The Mahasu Pahari language is an Indo-Aryan language spoken in the Mahasu region of Himachal Pradesh, India, primarily in the districts of Shimla, Solan, Sirmaur, and Kinnaur. It is one of the Western Pahari languages and is closely related to neighboring dialects such as Mandeali, Kangri, and Kullu Pahari. It serves as a means of communication for rural communities and is rich in oral traditions, including folk songs, tales, and proverbs. While Mahasu Pahari retains its prominence in rural areas, its usage is diminishing due to the rising influence of Hindi, the dominant language in the region.",
        "cultural_significance": "The language is a medium for folk songs, stories, and ballads that reflect the history, beliefs, and values of the Mahasu region. Traditional performances in Mahasu Pahari are an integral part of local festivals and rituals.",
        "linguistic_significance": "The language is often used in prayers and ceremonies dedicated to local deities, especially in temples of the Mahasu Devta, the chief deity of the region.",
    }

    open_button = tk.Button(root, text="Show Information on Mahasu Pahari Language", command=lambda: open_language_window(language_data))
    open_button.pack(expand=True, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()