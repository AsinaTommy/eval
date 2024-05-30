from projet.db import db


class Devis(db.Model):
    __tablename__ = 'devis'
    
    iddevis = db.Column(db.Integer, primary_key=True)
    idmaison = db.Column(db.Integer, db.ForeignKey('maison.idmaison'))
    idfinition = db.Column(db.Integer, db.ForeignKey('finition.idfinition'))
    idclient = db.Column(db.String(20))
    debuttravaux = db.Column(db.Date)
    augmentation = db.Column(db.Float)
    duree = db.Column(db.Float)
    datecreation = db.Column(db.Date)
    reference = db.Column(db.String(20))
    lieu = db.Column(db.String(40))
    
    maison = db.relationship('Maison')
    finition = db.relationship('Finition')
    
    def __init__(self, idmaison, idfinition, idclient, debuttravaux, augmentation, duree, datecreation,reference,lieu):
        self.idmaison = idmaison
        self.idfinition = idfinition
        self.idclient = idclient
        self.debuttravaux = debuttravaux
        self.augmentation = augmentation
        self.duree = duree
        self.datecreation = datecreation
        self.reference = reference
        self.lieu = lieu
    
    def json(self):
        return {'iddevis': self.iddevis,'maison': self.maison.json(), 'finition': self.finition.json(), 'idclient': self.idclient, 'debuttravaux': str(self.debuttravaux), 'augmentation': self.augmentation, 'duree': self.duree, 'datecreation': self.datecreation}
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(idclient=id)

    def save_to_db(self):
        db.session.add(self)

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
