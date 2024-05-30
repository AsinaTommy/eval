# from projet.db import db
# from sqlalchemy import text


# class Importe(db.Model):
#     __tablename__ = 'import'
    
#     id = db.Column(db.Integer, primary_key=True)
#     numseance=db.Column(db.Integer)
#     film=db.Column(db.String)
#     categorie=db.Column(db.String)
#     salle=db.Column(db.String)
#     date=db.Column(db.String)
#     heure=db.Column(db.String)    
#     def __init__(self, numseance , film, categorie, salle, date, heure):
#         self.numseance = numseance
#         self.film = film
#         self.categorie = categorie
#         self.salle = salle
#         self.date = date
#         self.heure = heure
        
#     def json(self):
#         return {'NumSeance': self.numseance, 'Film': self.film, 'Categorie': self.categorie, 'Salle': self.salle, 'Date': self.date, 'Heure': self.heure }
    
#     @classmethod
#     def find_all(cls):
#         return cls.query.all()
    
#     @classmethod
#     def find_by_name(cls, name):
#         return cls.query.filter_by(name=name).first()

#     def save_to_db(self):
#         db.session.add(self)
#         db.session.commit()

#     def delete_from_db(self):
#         db.session.delete(self)
#         db.session.commit()    
        
#     @classmethod    
#     def insertCategorie(cls):
#         db.session.execute(text("insert into categorie(libelle) select categorie from (select distinct categorie as categorie from import) vu where vu.categorie not in (select libelle from categorie)"))
#         # verifier na si efa ao??
    
#     @classmethod
#     def insertSalle(cls):
#         db.session.execute(text("insert into salle(numero) select distinct salle from import"))   
    
#     @classmethod
#     def insertFilm(cls):
#         db.session.execute(text("insert into film(titre,idcategorie) select distinct(film), idcategorie from (select * from import join categorie on import.categorie=categorie.libelle) as f"))    
    
#     @classmethod    
#     def insertSeance(cls):
#         db.session.execute(text("INSERT INTO seance (idfilm, idsalle, dateheure) SELECT idfilm, idsalle, to_timestamp(LEFT(TRIM(date), 10) || ' ' || heure, 'YYYY-MM-DD HH24:MI:SS') AS dateheure FROM last"))
        
#     @classmethod    
#     def insert_from_import(cls):
#         Importe.insertCategorie()
#         Importe.insertSalle()
#         Importe.insertFilm()
#         Importe.insertSeance()
#         db.session.commit()
        