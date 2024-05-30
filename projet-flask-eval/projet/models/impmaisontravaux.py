from projet.db import db

class ImportMaisonTravaux(db.Model):
    __tablename__ = 'importmaisontravaux'
   
    id = db.Column(db.Integer, primary_key=True)
    type_maison = db.Column(db.String)
    description = db.Column(db.String)
    surface = db.Column(db.Integer)
    code_travaux = db.Column(db.Integer)
    type_travaux = db.Column(db.String)
    unite = db.Column(db.String)
    prix_unitaire = db.Column(db.Float)
    quantite = db.Column(db.Float)
    duree_travaux = db.Column(db.Integer)
    
    def __init__(self, type_maison, description, surface, code_travaux, type_travaux, unite, prix_unitaire, quantite, duree_travaux):
        self.type_maison = type_maison
        self.description = description
        self.surface = surface
        self.code_travaux = code_travaux
        self.type_travaux = type_travaux
        self.unite = unite
        self.prix_unitaire = prix_unitaire
        self.quantite = quantite
        self.duree_travaux = duree_travaux
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()