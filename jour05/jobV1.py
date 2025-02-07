# Définissez une classe Part avec les attributs name (ex. "Mât") et material (ex. "Bois").
# ○ Ajoutez une méthode change_material(new_material) pour modifier le matériau.
# ○ Implémentez une méthode __str__ pour afficher une description de la pièce.

# Définissez une classe Ship avec un nom et un dictionnaire privé __parts contenant plusieurs instances de Part.
# ○ Ajoutez une méthode display_state() pour lister les pièces du bateau.
# ○ Implémentez une méthode replace_part(part_name, new_part) pour remplacer une pièce existante.
# Ajoutez une méthode change_part(part_name, new_material) pour changer directement le matériau d'une pièce existante.
# b. Montrez que les objets Part sont modifiés directement enmémoire. 

# Créez une classe RacingShip qui hérite de Ship.
# ○ Ajoutez un attribut supplémentaire max_speed.
# ○ Ajoutez une méthode display_speed() pour afficher la vitesse maximale.
# Créez un menu interactif avec des options pour remplacer des pièces, modifier des matériaux, ou afficher l'état du bateau.
# ○ Ajoutez un historique des modifications pour suivre l'évolution du bateau.

# Utilisez Tkinter pour créer une interface graphique simple permettant de remplacer les pièces ou de consulter l'état du bateau.
# Ajoutez des événements aléatoires (usure des pièces, tempêtes) pour enrichir la simulation.

# ==============================>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Les planches de bois : Chaque planche qui compose la coque du bateau.
# Les mâts et les voiles : Éléments essentiels pour la navigation.
# Les clous et les fixations : Maintiennent toutes les pièces ensemble.
# Les rames : Utilisées pour propulser le bateau.
# Les cordages : Utilisés pour attacher les voiles et d'autres parties du bateau.

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Ajouter l'importation nécessaire pour les images
import random

# Classe Part
class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        self.material = new_material

    def __str__(self):
        return f"{self.name} en {self.material}"

# Classe Ship
class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {}
        self.history = []  # Historique des modifications

    def add_part(self, part):
        self.__parts[part.name] = part

    def display_state(self):
        state = f"État du bateau {self.name}:\n"
        for part in self.__parts.values():
            state += str(part) + "\n"
        return state

    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.history.append(f"Remplacé {self.__parts[part_name]} par {new_part}")
            self.__parts[part_name] = new_part
        else:
            print(f"La pièce {part_name} n'existe pas.")

    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            old_material = self.__parts[part_name].material
            self.__parts[part_name].change_material(new_material)
            self.history.append(f"Changé le matériau de {part_name} de {old_material} à {new_material}")
        else:
            print(f"La pièce {part_name} n'existe pas.")

# Classe RacingShip héritant de Ship
class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        return f"Vitesse maximale : {self.max_speed} km/h"

# Simulation d'usure et d'événements aléatoires
def random_events(ship):
    events = ["usure", "tempête"]
    event = random.choice(events)
    part_name = random.choice(list(ship._Ship__parts.keys()))
    
    if event == "usure":
        print(f"Usure sur la pièce {part_name}!")
        ship.change_part(part_name, "Acier")  # Changer le matériau par défaut pour simuler l'usure
    elif event == "tempête":
        print(f"Tempête endommagée la pièce {part_name}!")
        ship.replace_part(part_name, Part(part_name, "Aluminium"))  # Remplacer par un matériau plus résistant

# Interface graphique avec Tkinter
class ShipApp:
    def __init__(self, master, ship):
        self.master = master
        self.ship = ship
        self.master.geometry("1280x720")
        self.master.title("Gestion du bateau")
        self.create_widgets()
        # Ajouter une image du bateau
        try:
            self.image = Image.open("cartes/bateauThesee.jpg")  # Remplacer par le chemin de l'image
            self.photo = ImageTk.PhotoImage(self.image)
            self.background_label = tk.Label(self.master, image=self.photo)
            self.background_label.pack()
        except Exception as e:
            print(f"Erreur lors du chargement de l'image : {e}")

        self.state_label = tk.Label(self.master, text="État du bateau:", bg="white", font=("Helvetica", 14))
        self.state_label.pack(pady=10)

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

   
    app = ShipApp(root, ship)
    root.mainloop()
