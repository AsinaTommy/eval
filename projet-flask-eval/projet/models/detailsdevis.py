from projet.db import db


class DetailDevis(db.Model):
    __tablename__ = 'detaildevis'
    
    iddetailsdevis = db.Column(db.Integer, primary_key=True)
    iddevis = db.Column(db.Integer, db.ForeignKey('devis.iddevis'))
    idtravaux = db.Column(db.Integer, db.ForeignKey('travaux.idtravaux'))
    quantite = db.Column(db.Float)
    pu = db.Column(db.Float)
    devis = db.relationship('Devis')
    travaux = db.relationship('Travaux')
    
    def __init__(self, iddevis, idtravaux, quantite, pu):
        self.iddevis = iddevis
        self.idtravaux = idtravaux
        self.quantite = quantite
        self.pu = pu
        
        
    def json(self):
        return {'devis': self.devis.json(), 'travaux': self.travaux.json(), 'quantite': self.quantite, 'pu': self.pu}
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(iddetailsdevis=id).first()

    def save_to_db(self):
        db.session.add(self)

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
