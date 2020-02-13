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


  ALTER TABLE inventory
    ADD CONSTRAINT fk_inv_product_id
    FOREIGN KEY (product_id)
    REFERENCES products (product_id)
    ON DELETE CASCADE;


    ALTER TABLE conferences
    ADD CONSTRAINT mere
    FOREIGN KEY (id_conferencier)
    REFERENCES conferenciers (id)
    ON DELETE CASCADE;
