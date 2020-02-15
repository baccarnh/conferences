from view.conferencier_view import *
from view.conference_view import *

auteur=ConferencierView()
discours=ConferenceView()
choice_table=""
choice_action=""

if __name__ == '__main__':


    while choice_table not in ["cf","cfcier","q"]:
        print("verifiez votre saisie cf cfcier ou q")
        choice_table = input("veuillez saisir le nom de la table sur la quelle vous voudriez agir\n"
                             "cf pour conferences\n "
                             "cfcier pour conferenciers \n"
                             " q pour quitter").lower()
    else:
        while choice_table !="q":

            if choice_table == "cf":
                while choice_action not in ["a","s","c"]:
                    print("verifiez votre saisie ")
                    choice_action = input("veuillez saisir: \n"
                                "A pour ajouter une conference \n"
                                "S pour supprimer une conference \n"
                                "C pour consulter une conference").lower()
                else:
                    if choice_action=="a":
                        discours.add_conference()
                    if choice_action=="s":
                        discours.delete_conference()
                    if choice_action=="c":
                        discours.display_conference()
            if choice_table=="cfcier":

                while choice_action not in ["a","s","c"]:
                    print("verifiez votre saisie ")
                    choice_action = input("veuillez saisir: \n"
                                "A pour ajouter une conference \n"
                                "S pour supprimer une conference \n"
                                "C pour consulter une conference").lower()
                else:
                    if choice_action == "a":
                        auteur.add_conferencier()
                    if choice_action == "s":
                        auteur.delete_conferencier()
                    if choice_action == "c":
                        auteur.display_conferencier()

            exit()