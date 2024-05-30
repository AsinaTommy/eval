from projet.db import db

class Maison(db.Model):
    __tablename__ = 'maison'
    
    idmaison = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(30))
    duree = db.Column(db.Float)
    surface = db.Column(db.Float)
    descriptions = db.Column(db.String)
    
    def json(self):
        des = self.descriptions.split(',')
        return {'id': self.idmaison, 'libelle': self.libelle, 'duree': self.duree, 'surface':self.surface, 'descriptions':des}
    
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