"""
Créer une classe pour représenter un joueur ainsi qu'une classe pour représenter une équipe de foot.
La classe Joueur doit avoir les attributs suivants : nom, numéro, position, nombre de buts marqués, 
passes décisives effectuées, cartons jaunes reçus et cartons rouges reçus. Tous ces attributs 
doivent être initialisés lors de la création de l’objet Joueur.

Cette classe doit posséder les méthodes suivantes :
➔ marquerUnBut,
➔ effectuerUnePasseDecisive,
➔ recevoirUnCartonJaune,
➔ recevoirUnCartonRouge,
➔ afficherStatistiques.

Ces méthodes permettent de mettre à jour les statistiques du joueur.

La classe Equipe doit avoir les attributs nom et liste de joueurs. Le nom de l’équipe et la liste 
de joueurs (liste vide par défaut) doivent être initialisés dans le constructeur.

Ajouter les méthodes suivantes dans la classe Equipe :
- ajouterJoueur : cette méthode ajoute un joueur à l’équipe.
- AfficherStatistiquesJoueurs : cette méthode permet d’afficher toutes les statistiques de l’ensemble des joueurs.
- mettreAJourStatistiquesJoueur : cette méthode permet de mettre à jour les statistiques d’un joueur (buts, cartons ...).

Créez plusieurs joueurs avec les paramètres de votre choix et ajoutez-les aux équipes.

Présenter l’ensemble des joueurs de chaque équipe. Utiliser les différentes méthodes 
afin de simuler un match, marquer un but, avoir un carton rouge...
Et afficher à nouveau les statistiques des joueurs.
"""

class Joueur:
    def __init__(self, nom, numero, position, buts, passes_decisives, cartons_jaunes, cartons_rouges):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = buts
        self.passes_decisives = passes_decisives
        self.cartons_jaunes = cartons_jaunes
        self.cartons_rouges = cartons_rouges

    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        return f'{self.nom} (#{self.numero}, {self.position}) - Buts: {self.buts}, Passes décisives: {self.passes_decisives}, Cartons Jaunes: {self.cartons_jaunes}, Cartons Rouges: {self.cartons_rouges}'

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def AfficherStatistiquesJoueurs(self):
        for joueur in self.joueurs:
            print(joueur.afficherStatistiques())

    def mettreAJourStatistiquesJoueur(self, nom, buts=0, passes_decisives=0, cartons_jaunes=0, cartons_rouges=0):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                joueur.buts += buts
                joueur.passes_decisives += passes_decisives
                joueur.cartons_jaunes += cartons_jaunes
                joueur.cartons_rouges += cartons_rouges

# Créer des joueurs
joueur1 = Joueur("John", 10, "Attaquant", 5, 3, 1, 0)
joueur2 = Joueur("Paul", 8, "Milieu", 2, 5, 2, 1)
joueur3 = Joueur("George", 4, "Défenseur", 0, 1, 3, 0)

# Créer deux équipes
equipe = Equipe("OM")
equipe1 = Equipe("PSG")

# Ajouter des joueurs à l'équipe
equipe.ajouterJoueur(joueur1)
equipe.ajouterJoueur(joueur2)
equipe1.ajouterJoueur(joueur3)

# Afficher les statistiques des joueurs avant le match
print("Statistiques des joueurs avant le match:")
equipe.AfficherStatistiquesJoueurs()
equipe1.AfficherStatistiquesJoueurs()

# Simuler un match
joueur1.marquerUnBut()
joueur2.recevoirUnCartonJaune()
joueur3.recevoirUnCartonRouge()
joueur1.effectuerUnePasseDecisive()

# Afficher les statistiques des joueurs après le match
print("\nStatistiques des joueurs après le match:")
equipe.AfficherStatistiquesJoueurs()
equipe1.AfficherStatistiquesJoueurs()