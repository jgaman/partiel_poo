# une classe eleve avec les attributs privés nom, prenom, notes, nationalité et un id unique et getter pour chaque attribut et un setter pour chaque attribut sauf l'id
import random


class Etudiant:

    """La classe `Etudiant` est un schéma de création d'objets représentant un etudiant
    :param nom: nom de l'etudiant 
    :type nom: str
    :param prenom: prenom de l'etudiant
    :type prenom: str
    :param identifiant: identifiant de l'etudiant
    :type identifiant: int
    :param notes: liste des notes de l'etudiant
    :type notes: list
    :param nationalite: nationalite de l'etudiant
    :type nationalite: dict
    elle contient les methodes suivantes:
    - ajouter_note: ajoute une note à la liste des notes de l'etudiant
    - afficher_moyenne: retourne la moyenne de l'etudiant
    - afficher_notes: retourne toutes les notes de l'etudiant
    - __str__: retourne le nom, le prenom, les notes, la nationalité et l'id de l'etudiant quand on imprime un
    - objet de type Etudiant
    - __get__: retourne la valeur de l'attribut de l'etudiant
    - __set__: modifie la valeur de l'attribut de l'etudiant

    """

    def __init__(self, nom: str, prenom: str, identifiant: int, notes: list, nationalite: dict):
        '''Constructeur de la classe Etudiant qui prend en paramètre le nom, le prenom, les notes, la nationalité et l'id de l'élève'''
        self.__nom = nom
        self.__prenom = prenom
        self.__notes = notes
        self.__nationalite = nationalite
        self.__id = identifiant

    def __get__(self, instance, owner):
        '''Retourne la valeur de l'attribut de l'élève'''
        return self.__dict__[instance]

    def __set__(self, instance, value):
        '''Modifie la valeur de l'attribut de l'élève'''
        self.__dict__[instance] = value

    def __str__(self):
        '''Retourne le nom, le prenom, les notes, la nationalité et l'id de l'élève quand on imprime un
        objet de type Etudiant'''

        return f"🤓 Nom: {self.__nom}, Prenom: {self.__prenom}, Notes: {self.__notes}, Nationalite: {self.__nationalite}, ID: {self.__id}"

    def ajouter_note(self, note: int):
        '''Ajoute une note à la liste des notes de l'élève'''

        self.__notes.append(note)

    def afficher_moyenne(self):
        '''Retourne la moyenne de l'élève'''

        return sum(self.__notes)/len(self.__notes)

    def afficher_notes(self):
        '''Retourne toutes les notes de l'élève'''

        return f"les notes de l'élève: {self.__nom} sont: {self.__notes}"


class Promotion:
    '''La classe `Promotion` est un schéma de création d'objets représentant une promotion
    elle contient les methodes suivantes:
    - ajouter_etudiant: ajoute un élève à la liste des élèves de la promotion
    - retirer_etudiant: retire un élève de la liste des élèves de la promotion
    - afficher_etudiants: retourne tous les élèves de la promotion
    - afficher_moyenne_promotion: retourne la moyenne de la promotion'''

    def __init__(self, nom: str, etudiants: list):
        '''Constructeur de la classe Promotion qui prend en paramètre le nom et la liste des élèves de la promotion'''

        self.__nom = nom
        self.__etudiants = etudiants

    def ajouter_etudiant(self, etudiant: Etudiant):
        '''Ajoute un élève à la liste des élèves de la promotion'''

        self.__etudiants.append(etudiant)

    def retirer_etudiant(self, etudiant: Etudiant):
        '''Retire un élève de la liste des élèves de la promotion'''

        self.__etudiants.remove(etudiant)

    def afficher_etudiants(self):
        '''Retourne tous les élèves de la promotion'''

        for etudiant in self.__etudiants:
            print(etudiant)

    def afficher_moyenne_promotion(self):
        '''Retourne la moyenne de la promotion'''
        return sum([etudiant.afficher_moyenne() for etudiant in self.__etudiants])/len(self.__etudiants)

    def passer_examen(self, nom_matiere: str):
        '''ajoute une note aléatoire de passage
pour la matière spécifiée à tous les étudiants de la promotion'''

        for etudiant in self.__etudiants:
            etudiant.ajouter_note(random.randint(5, 20))
            return f"📝 Les Etudiants de la Promo {self.__nom} ont passé l'examen: {nom_matiere}"

    def afficher_reussite(self):
        '''affiche les étudiants dont les notes aux examens sont supérieures ou égales à 10'''

        print("📝 Les Etudiants de la Promo qui ont réussi sont: ")
        for etudiant in self.__etudiants:
            if etudiant.afficher_moyenne() >= 10:
                print(etudiant)
            else:
                pass


# Création d'objets de type Etudiant
Mat = Etudiant("Mat", "Luc", 1, [10, 12, 14], {
               "pays": "France", "ville": "Lyon"})
Nour = Etudiant("Nour", "El", 2, [14, 13, 10], {
                "pays": "Maroc", "ville": "Marakech"})
Jean = Etudiant("Jean", "Marc", 3, [14, 16, 14], {
                "pays": "Côte d'ivoire", "ville": "Abidjan"})
Paul = Etudiant("Paul", "Rim", 4, [15, 12, 16], {
                "pays": "France", "ville": "Paris"})
Rahim = Etudiant("Rahim", "El", 5, [14, 13, 10], {
                 "pays": "Esi", "ville": "Langueux"})

# teste des différentes méthodes de la classe Etudiant
print(Rahim.afficher_notes())
print(Paul.afficher_moyenne())
print(Mat)

# utilisons la methode ajouter_note pour ajouter une note à un élève
Mat.ajouter_note(15)
Nour.ajouter_note(12)
Jean.ajouter_note(11)
Paul.ajouter_note(13)
Rahim.ajouter_note(17)

print(Paul.afficher_notes())

# Création d'objets de type Promotion
Gema = Promotion("Gema", [Mat, Nour, Jean, Paul, Rahim])

# affichage des élèves de la promotion Gema
print(Gema.afficher_etudiants())

# affichage de la moyenne de la promotion Gema
print(Gema.afficher_moyenne_promotion())

print("---------------------BONUS---------------------------------")
# passage d'un examen de Python pour la promotion Gema
print(Gema.passer_examen("Python"))
print(Gema.afficher_reussite())

print("---------------------BONUS---------------------------------")
# passage d'un examen de Java pour la promotion Gema
print(Gema.passer_examen("Java"))
print(Gema.afficher_reussite())
