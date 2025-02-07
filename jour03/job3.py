"""
Dans cet exercice, vous allez créer votre to do list.

Créer une classe Tache qui représente une tâche à faire. Cette classe a
comme attribut un titre, une description et un statut (à faire ou terminer)
initialisés dans le constructeur.

Créer une classe ListeDeTaches qui représente la liste des tâches à faire ainsi
que toutes les méthodes nécessaires à la gestion de celles-ci avec comme
attribut taches(liste).

Ajouter les méthodes suivantes :
➔ ajouterTache : qui permet d’ajouter une tâche.
➔ supprimerTache : qui permet de supprimer une tâche.
➔ marquerCommeFinie : qui permet de signaler que la tâche est faite.
➔ afficherListe : qui permet de retourner une liste de toutes les tâches.
➔ filterListe : qui permet de filtrer les tâches par rapport à un statut et
retourne cette liste.

Tester votre code en créant plusieurs instances de Tache, les ajouter à la
classe listeDeTache, supprimer une tache, changer le statut d’une tâche,
afficher toutes les tâches et afficher les tâches à faire."""


class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def marquerCommeFinie(self):
        self.statut = "terminée"

    def __str__(self):
        return f"Titre: {self.titre}, Description: {self.description}, Statut: {self.statut}"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        self.taches = [tache for tache in self.taches if tache.titre != titre]

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.marquerCommeFinie()

    def afficherListe(self):
        return [str(tache) for tache in self.taches]

    def filterListe(self, statut):
        return [str(tache) for tache in self.taches if tache.statut == statut]

# Tester le code
tache1 = Tache("Apprendre Python", "Compléter le cours en ligne")
tache2 = Tache("Faire les courses", "Acheter des légumes")
tache3 = Tache("Lecture", "Lire 20 pages d'un livre")

listeDeTaches = ListeDeTaches()
listeDeTaches.ajouterTache(tache1)
listeDeTaches.ajouterTache(tache2)
listeDeTaches.ajouterTache(tache3)

listeDeTaches.supprimerTache("Faire les courses")
listeDeTaches.marquerCommeFinie("Apprendre Python")

print("Toutes les tâches:")
print(listeDeTaches.afficherListe())

print("Tâches à faire:")
print(listeDeTaches.filterListe("à faire"))

print("Tâches terminées:")
print(listeDeTaches.filterListe("terminée"))


