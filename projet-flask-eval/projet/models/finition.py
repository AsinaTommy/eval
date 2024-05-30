from projet.db import db

class Finition(db.Model):
    __tablename__ = 'finition'
    
    idfinition = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(30))
    augmentation = db.Column(db.Float)
    
    def __init__(self,  libelle, augme):
        self.libelle = libelle
        self.augmentation = augme
        
    
    def json(self):
        return {'id': self.idfinition,'libelle': self.libelle, 'augmentation': self.augmentation}
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(idfinition=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()