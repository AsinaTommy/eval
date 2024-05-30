from projet.db import db

class Histogramme(db.Model):
    __tablename__ = 'histogramme'
    __table_args__ = {'info': dict(is_view=True)}
    
    ligne = db.Column(db.Integer, primary_key=True)
    annee = db.Column(db.Integer)
    moi = db.Column(db.String(30))
    libelle = db.Column(db.String(30))
    montant = db.Column(db.Float)
    
    