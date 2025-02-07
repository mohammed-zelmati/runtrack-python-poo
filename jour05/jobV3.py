import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Ajouter l'importation nécessaire pour les images
import random

# Classe pour les pièces du bateau
class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def __str__(self):
        return f"{self.name} ({self.material})"

# Classe pour le bateau
class RacingShip:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.parts = []
        self.history = []

    def add_part(self, part):
        self.parts.append(part)
        self.history.append(f"Ajout de la pièce {part}")

    def replace_part(self, part_name, new_part):
        for i, part in enumerate(self.parts):
            if part.name == part_name:
                old_part = self.parts[i]
                self.parts[i] = new_part
                self.history.append(f"Remplacement de la pièce {old_part} par {new_part}")
                return
        self.history.append(f"Erreur : La pièce {part_name} n'a pas été trouvée.")

    def display_state(self):
        state = f"Bateau : {self.name}\nVitesse : {self.speed} km/h\n\n"
        state += "Pièces :\n"
        for part in self.parts:
            state += f"- {part}\n"
        return state

# Fonction pour générer des événements aléatoires
def random_events(ship):
    events = [
        "Une tempête a endommagé une pièce.",
        "Le bateau a reçu une réparation de la coque.",
        "Un pirate a attaqué le bateau, mais a été repoussé.",
        "Une pièce a été volée par des inconnus."
    ]
    event = random.choice(events)
    ship.history.append(event)
    messagebox.showinfo("Événement Aléatoire", event)

# Classe pour l'application Tkinter
class ShipApp:
    def __init__(self, master, ship):
        self.master = master
        self.ship = ship
        self.master.geometry("1280x720")
        self.master.title("Gestion du Bateau")
        self.create_widgets()

    def create_widgets(self):
        # Boutons pour afficher l'état du bateau et l'historique
        self.state_button = tk.Button(self.master, text="Afficher l'état du bateau", command=self.show_state)
        self.state_button.pack(pady=10)

        self.history_button = tk.Button(self.master, text="Afficher l'historique des modifications", command=self.show_history)
        self.history_button.pack(pady=10)

        # Entry pour ajouter ou remplacer des pièces
        self.part_name_entry = tk.Entry(self.master)
        self.part_name_entry.pack(pady=10)
        self.part_name_entry.insert(0, "Nom de la pièce")

        self.material_entry = tk.Entry(self.master)
        self.material_entry.pack(pady=10)
        self.material_entry.insert(0, "Matériau")

        self.add_part_button = tk.Button(self.master, text="Ajouter une pièce", command=self.add_part)
        self.add_part_button.pack(pady=10)

        self.replace_part_button = tk.Button(self.master, text="Remplacer une pièce", command=self.replace_part)
        self.replace_part_button.pack(pady=10)

        # Bouton pour générer un événement aléatoire
        self.random_event_button = tk.Button(self.master, text="Générer un événement aléatoire", command=self.random_event)
        self.random_event_button.pack(pady=10)

        # Ajouter une image du bateau
        try:
            self.image = Image.open("cartes/bateauThesee.jpg")  # Remplacer par le chemin de l'image
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label = tk.Label(self.master, image=self.photo)
            self.image_label.pack()
        except Exception as e:
            print(f"Erreur lors du chargement de l'image : {e}")

    def show_state(self):
        state = self.ship.display_state()
        messagebox.showinfo("État du Bateau", state)

    def show_history(self):
        history = "\n".join(self.ship.history)
        messagebox.showinfo("Historique des Modifications", history)

    def add_part(self):
        name = self.part_name_entry.get()
        material = self.material_entry.get()
        new_part = Part(name, material)
        self.ship.add_part(new_part)
        messagebox.showinfo("Pièce Ajoutée", f"La pièce {new_part} a été ajoutée.")

    def replace_part(self):
        part_name = self.part_name_entry.get()
        material = self.material_entry.get()
        new_part = Part(part_name, material)
        self.ship.replace_part(part_name, new_part)
        messagebox.showinfo("Pièce Remplacée", f"La pièce {part_name} a été remplacée par {new_part}.")

    def random_event(self):
        random_events(self.ship)

# Exemple d'utilisation
if __name__ == "__main__":
    # Créer un bateau et l'ajouter à l'interface
    ship = RacingShip("Vaisseau Éclair", 500)
    ship.add_part(Part("Mât", "Bois"))
    ship.add_part(Part("Coque", "Acier"))
    ship.add_part(Part("Voile", "Tissu"))
    
    # Création de la fenêtre Tkinter
    root = tk.Tk()

    # Créer l'application
    app = ShipApp(root, ship)
    root.mainloop()
