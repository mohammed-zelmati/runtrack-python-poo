import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Ajouter l'importation nécessaire pour les images

class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        self.material = new_material

    def __str__(self):
        return f"{self.name} en {self.material}"

class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {}

    def add_part(self, part):
        self.__parts[part.name] = part

    def display_state(self):
        return "\n".join([str(part) for part in self.__parts.values()])

    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.__parts[part_name] = new_part
            return f"{part_name} remplacé par {new_part.name}"
        else:
            return f"{part_name} non trouvé"

    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            self.__parts[part_name].change_material(new_material)
            return f"Matériau de {part_name} changé en {new_material}"
        else:
            return f"{part_name} non trouvé"

    def get_part(self, part_name):
        return self.__parts.get(part_name)

class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        return f"Vitesse maximale: {self.max_speed} nœuds"

class ShipGUI:
    def __init__(self, master, ship):
        self.master = master
        self.ship = ship
        self.history = []

        self.master.geometry("1280x720")
        self.master.title("Simulateur de Bateau")

        # Ajout de l'image du bateau
        try:
            # Chargez l'image
            self.image = Image.open("cartes/bateauThesee.jpg")  # Remplacez par le bon chemin de l'image
            self.master.update()  # Mettez à jour la fenêtre pour obtenir sa taille
            # width = self.master.winfo_width()
            # height = self.master.winfo_height()

            width = 600
            height = 720

            # Redimensionnez l'image selon la taille de la fenêtre
            self.image = self.image.resize((width, height))
            self.photo = ImageTk.PhotoImage(self.image)

            # Créez un label pour l'image de fond et placez-le sur toute la fenêtre
            self.background_label = tk.Label(self.master, image=self.photo)
            self.background_label.place(relwidth=1, relheight=1)  # Étend l'image sur toute la fenêtre

        except Exception as e:
            print(f"Erreur lors du chargement de l'image : {e}")

        # Frame pour contenir tous les éléments à droite
        self.right_frame = tk.Frame(self.master, bg="white", padx=10, pady=10)
        self.right_frame.place(relx=0.75, rely=0.05, relwidth=0.25, relheight=0.9)

        # Ajouter les widgets à droite
        self.state_label = tk.Label(self.right_frame, text="État du bateau:", bg="white", font=("Helvetica", 14))
        self.state_label.pack(pady=10)

        self.state_text = tk.Text(self.right_frame, height=10, width=50)
        self.state_text.pack(pady=10)

        self.replace_frame = tk.Frame(self.right_frame, bg="white")
        self.replace_frame.pack(pady=10)

        self.part_name_label = tk.Label(self.replace_frame, text="Nom de la pièce:", bg="white")
        self.part_name_label.grid(row=0, column=0)

        self.part_name_entry = tk.Entry(self.replace_frame)
        self.part_name_entry.grid(row=0, column=1)

        self.new_part_name_label = tk.Label(self.replace_frame, text="Nouveau nom:", bg="white")
        self.new_part_name_label.grid(row=1, column=0)

        self.new_part_name_entry = tk.Entry(self.replace_frame)
        self.new_part_name_entry.grid(row=1, column=1)

        self.new_part_material_label = tk.Label(self.replace_frame, text="Nouveau matériau:", bg="white")
        self.new_part_material_label.grid(row=2, column=0)

        self.new_part_material_entry = tk.Entry(self.replace_frame)
        self.new_part_material_entry.grid(row=2, column=1)

        self.replace_button = tk.Button(self.replace_frame, text="Remplacer", command=self.replace_part)
        self.replace_button.grid(row=3, column=0, columnspan=2)

        self.change_frame = tk.Frame(self.right_frame, bg="white")
        self.change_frame.pack(pady=10)

        self.change_part_name_label = tk.Label(self.change_frame, text="Nom de la pièce:", bg="white")
        self.change_part_name_label.grid(row=0, column=0)

        self.change_part_name_entry = tk.Entry(self.change_frame)
        self.change_part_name_entry.grid(row=0, column=1)

        self.new_material_label = tk.Label(self.change_frame, text="Nouveau matériau:", bg="white")
        self.new_material_label.grid(row=1, column=0)

        self.new_material_entry = tk.Entry(self.change_frame)
        self.new_material_entry.grid(row=1, column=1)

        self.change_button = tk.Button(self.change_frame, text="Changer", command=self.change_material)
        self.change_button.grid(row=2, column=0, columnspan=2)

        self.history_button = tk.Button(self.right_frame, text="Afficher l'historique", command=self.show_history)
        self.history_button.pack(pady=10)

        self.update_state()

    def update_state(self):
        self.state_text.delete(1.0, tk.END)
        self.state_text.insert(tk.END, self.ship.display_state())

    def replace_part(self):
        part_name = self.part_name_entry.get()
        new_part_name = self.new_part_name_entry.get()
        new_part_material = self.new_part_material_entry.get()
        new_part = Part(new_part_name, new_part_material)
        result = self.ship.replace_part(part_name, new_part)
        self.history.append(f"Pièce remplacée: {part_name} -> {new_part_name}")
        messagebox.showinfo("Résultat", result)
        self.update_state()

    def change_material(self):
        part_name = self.change_part_name_entry.get()
        new_material = self.new_material_entry.get()
        result = self.ship.change_part(part_name, new_material)
        self.history.append(f"Matériau changé: {part_name} -> {new_material}")
        messagebox.showinfo("Résultat", result)
        self.update_state()

    def show_history(self):
        messagebox.showinfo("Historique", "\n".join(self.history))

    def run(self):
        self.master.mainloop()

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'un bateau de course
    ship = RacingShip("Black Pearl", 50)
    ship.add_part(Part("Mât", "Bois"))
    ship.add_part(Part("Voile", "Toile"))
    ship.add_part(Part("Coque", "Acier"))
    ship.add_part(Part("Rame", "Bois"))
    ship.add_part(Part("Planche", "Bois"))
    ship.add_part(Part("Cordage", "Toile"))
    ship.add_part(Part("Clous", "Acier"))

    # Simulation en mode graphique
    root = tk.Tk()
    gui = ShipGUI(root, ship)
    gui.run()