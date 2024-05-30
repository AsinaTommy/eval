from projet.db import db

class ImportDevis(db.Model):
    __tablename__ = 'importdevis'
   
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String)
    ref_devis = db.Column(db.String)
    type_maison = db.Column(db.String)
    finition = db.Column(db.String)
    taux_finition = db.Column(db.Float)
    date_devis = db.Column(db.Date)
    date_debut = db.Column(db.Date)
    lieu = db.Column(db.String)

    def __init__(self, client, ref_devis, type_maison, finition, taux_finition, date_devis, date_debut, lieu):
        self.client = client
        self.ref_devis = ref_devis
        self.type_maison = type_maison
        self.finition = finition
        self.taux_finition = taux_finition
        self.date_devis = date_devis
        self.date_debut = date_debut
        self.lieu = lieu
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
