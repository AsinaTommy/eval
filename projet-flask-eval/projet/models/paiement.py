from projet.db import db

class Paiement(db.Model):
    __tablename__ = 'paiement'
    
    idpaiement = db.Column(db.Integer, primary_key=True)
    iddevis = db.Column(db.Integer, db.ForeignKey('devis.iddevis'))
    montant = db.Column(db.Float)
    dateheure = db.Column(db.Date)
    devis = db.relationship('Devis')
    reference = db.Column(db.String(30))
    
    def json(self):
        return {'devis': self.devis.json(), 'montant': self.montant, 'dateheure': str(self.dateheure), 'reference': self.reference}
    
    
    def __init__(self, iddevis, montant, dateheure, references ):
        self.iddevis = iddevis
        self.montant = montant
        self.dateheure = dateheure
        self.reference = references
        
        
        
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(iddevis=id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
