# data base creation
creatdb hotel
psql hotel

CREATE TABLE conferenciers (
  id SERIAL PRIMARY KEY NOT NULL,
  prenom VARCHAR (20) NOT NULL,
  nom VARCHAR (20) NOT NULL,
  description VARCHAR (250),
  profession VARCHAR (20) NOT NULL,
  satut_actif BOOLEAN NOT NULL );

  
CREATE TABLE conferences (
  id SERIAL PRIMARY KEY NOT NULL,
  titre VARCHAR (50) NOT NULL,
  resume VARCHAR (250) ,
  date DATE NOT NULL,
  heure TIME NOT NULL,
  date_creation date,
  id_conferencier INTEGER NOT NULL );
