from .conferencier_hyd import*
#auteur=Conferencier():
class HydConference:
    def __init__(self, dico):
        self.id=None
        self.titre = None
        self.resume = None
        self.date = None
        self.heure= None
        self.date_creation = None
        self.id_conferencier=None
        self.prenom=None
        self.nom=None
        self.hydrate(dico)

    def hydrate(self,dico):
        for key, value in dico.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        return"""------------------\n \
            id: {}\n \
            titre: {}\n \
            resume: {}\n \
            date: {}\n \
            heure: {}\n \
            date_creation: {}\n \
            id_conferencier: {}\n\
            prenom:{}\n\
            nom:{}\n""" .format(self.id, self.titre, self.resume, self.date, self.heure, self.date_creation, self.id_conferencier, self.prenom, self.nom)

