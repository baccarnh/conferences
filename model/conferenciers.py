from model.connection import Connection
from model.entities.conferencier_hyd import HydConferencier

class Conferencier():
    def __init__(self):
        self.db = Connection()

    def add_conferencier(self, prenom, nom, description, profession):
        """method adding conferencier"""
        argument=(prenom, nom, description, profession)
        sql="""INSERT INTO conferenciers (prenom, nom, description, profession) VALUES (%s,%s,%s,%s);"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql, argument)
        self.db.connection.commit()
        self.db.close_connection()

    def delete_conferencier(self, id):
        """method deleting conferencier"""
        sql="""DELETE FROM conferenciers WHERE id=%s;"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (id,))
        self.db.connection.commit()
        self.db.close_connection()

    def display_conferencier(self):
        '''method selecting all conferenciers that have actif status'''
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM conferenciers WHERE statut_actif=True ;")
        actif_conferenciers = self.db.cursor.fetchall()
        for key, value in enumerate(actif_conferenciers):
            actif_conferenciers[key]=HydConferencier(value)

        self.db.close_connection()

        return actif_conferenciers