from model.conferences import *

class ConferenceView:
    discours = Conference()
    def __init__(self):
        pass

    def add_conference(self):
        titre=input("veuillez saisir le titre:")
        resume=input("veuillez saisir le resume:")
        date=input("veuillez saisir la date:").strftime("%d/%m/%Y")
        heure=input("veuillez saisir l'heure:").strftime("%H:%M")
        date_creation=input("veuillez saisir la date de creation: ")
        id_conferencier=input ("veuillez preciser le id du conferencier conrrespondant")
        self.discours.add_conference(titre, resume, date, heure, date_creation, id_conferencier)

    def delete_conference(self):
        id=input("veuillez saisir le id de la conference qu'il faut supprimer")
        self.discours.delete_conference(id)

    def display_conference(self):
        list_discours=self.discours.display_conference()
        for ele in list_discours:
            print("********************************\n"
            "{}".format(ele))