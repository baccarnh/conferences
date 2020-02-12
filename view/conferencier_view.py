from model.conferenciers import *

class ConferencierView:
    auteur = Conferencier()
    def __init__(self):
        pass

    def add_conferencier(self):
        prenom=input("veuillez saisir le prenom:")
        nom=input("veuillez saisirle nom:")
        description=input("veuillez saisirla description:")
        profession=input("veuillez saisirla profession:")
        self.auteur.add_conferencier(prenom, nom, description, profession)
