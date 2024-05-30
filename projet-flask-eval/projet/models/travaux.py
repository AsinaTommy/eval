from projet.db import db

class Travaux(db.Model):
    __tablename__ = 'travaux'
    
    idtravaux = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(100))
    unite = db.Column(db.String(20))
    pu = db.Column(db.Float)
    code = db.Column(db.String(20))
    
    
    def __init__(self, libelle, unite, pu, code):
        self.libelle = libelle
        self.unite = unite
        self.code = code
        self.pu = pu
        
    
    def json(self):
        return {'libelle': self.libelle, 'unite': self.unite, 'pu': self.pu, 'code': self.code}
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(idtravaux=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()