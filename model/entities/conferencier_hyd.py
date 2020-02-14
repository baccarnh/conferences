class HydConferencier:
    def __init__(self, dico):
        self.id=None
        self.prenom = None
        self.nom = None
        self.description = None
        self.profession= None
        self.hydrate(dico)

    def hydrate(self,dico):
        for key, value in dico.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        return"""------------------\n \
            id: {}\n \
            prenom: {}\n \
            nokm: {}\n \
            description : {}\n \
            profession: {}\n """.format(self.id, self.prenom, self.nom, self.description, self.profession)
