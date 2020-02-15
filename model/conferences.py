from model.connection import Connection
from model.entities.conference_hyd import HydConference

class Conference():
    def __init__(self):
        self.db = Connection()

    def add_conference(self, titre, resume, date, heure, date_creation, id_conferencier):
        """method adding conference"""
        argument=(titre, resume, date, heure, date_creation, id_conferencier)
        sql="""INSERT INTO conferences (titre, resume, date, heure, date_creation, id_conferencier) VALUES (%s,%s,%s,%s,now(),%s);"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql, argument)
        self.db.connection.commit()
        self.db.close_connection()

    def delete_conference(self, id):
        """method deleting conference"""
        sql="""DELETE FROM conferences WHERE id=%s;"""
        self.db.initialize_connection()
        self.db.cursor.execute(sql, (id,))
        self.db.connection.commit()
        self.db.close_connection()

    def display_conference(self):
        '''method selecting all conferences with the nom prenom of conferencier having the id_conferencier valable'''
        SQL = " SELECT conferences.*, conferenciers.prenom, conferenciers.nom " \
              " FROM conferences INNER JOIN conferenciers" \
              " ON conferences.id_conferencier=conferenciers.id " \
              " ORDER BY conferences.date;"

        """SELECT a.*, b.prenom, b.prenom
        From conferences as a INNER JOIN conferenciers as b
        ON a.id_conferencier=b.id;"""

        self.db.initialize_connection()
        self.db.cursor.execute(SQL)
        all_conferences = self.db.cursor.fetchall()
        print(all_conferences)
        self.db.close_connection()
        for key, value in enumerate (all_conferences):
            all_conferences[key]=HydConference(value)
        return all_conferences