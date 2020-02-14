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

    def delete_conferencier(self):
        id=input("veuillez saisir le id du conferencier a supprimer")
        self.auteur.delete_conferencier(id)

    def display_conferencier(self):
        list_conf=self.auteur.display_conferencier()
        if list_conf ==[]:
            print ("aucun conferencier actif")
        else:
            for ele in list_conf:
                print("**************\n"
                      "{}".format(ele))