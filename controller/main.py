from view.conferencier_view import *
from view.conference_view import *

auteur=ConferencierView()
discours=ConferenceView()
choice_table=""
choice_action=""

if __name__ == '__main__':

    choice_table = input("veuillez saisir le nom de la table sur la quelle vous voudriez agir\n"
                         "cf pour conferences\n "
                         "cfcier pour conferenciers \n"
                         "tapez q pour quitter").lower()

    while choice_table != 'q':

        if choice_table == 'cf':
            choice_action = input("veuillez saisir: \n"
                            "A pour ajouter une conference \n"
                            "S pour supprimer une conference \n"
                            "C pour consulter une conference").lower()
            if choice_action=="a":
                discours.add_conference()
            if choice_action=="s":
                discours.delete_conference()
            if choice_action=="c":
                discours.display_conference()
        if choice_table=="cfcier":
            choice_action = input("veuillez saisir: \n "
                                  "A pour ajouter un conferencier \n "
                                  "S pour supprimer un conferencier \n"
                                  "C pour consulter un conferencier").lower()
            if choice_action == "a":
                auteur.add_conferencier()
            if choice_action == "s":
                auteur.delete_conferencier()
            if choice_action == "c":
                auteur.display_conferencier()

        exit()