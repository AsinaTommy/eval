from projet.db import db

class MaisonTravaux(db.Model):
    __tablename__ = 'maisontravaux'
    
    idmaisontravaux = db.Column(db.Integer, primary_key=True)
    idmaison = db.Column(db.Integer, db.ForeignKey('maison.idmaison'))
    idtravaux = db.Column(db.Integer, db.ForeignKey('travaux.idtravaux'))
    quantite = db.Column(db.Float)
    maison = db.relationship('Maison')
    travaux = db.relationship('Travaux')
    
    def json(self):
        return {'maison': self.maison.json(), 'travaux': self.travaux.json(), 'quantite': self.quantite}
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(idmaison=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()