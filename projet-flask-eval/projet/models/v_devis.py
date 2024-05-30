from projet.db import db


class V_devis(db.Model):
    __tablename__ = 'v_devis'
    __table_args__ = {'info': dict(is_view=True)}

    iddevis = db.Column(db.Integer, primary_key=True)
    idclient = db.Column(db.Integer, primary_key=True)
    maison = db.Column(db.String(30))
    finition = db.Column(db.String(30))
    total = db.Column(db.Numeric(10, 2))
    paye = db.Column(db.Numeric(10, 2))
    reste = db.Column(db.Numeric(10, 2))
    debut = db.Column(db.Date)
    fin = db.Column(db.Date)

    def __init__(self, idclient, iddevis, maison, finition, total, paye, debut, fin, reste):
        self.idclient = idclient
        self.iddevis = iddevis
        self.maison = maison
        self.finition = finition
        self.total = total
        self.paye = paye
        self.reste = reste
        self.debut = debut
        self.fin = fin

        
    def json(self):
        couleur = ['red','green']
        return {
            'idclient': self.idclient,
            'iddevis': self.iddevis,
            'maison': self.maison,
            'finition': self.finition,
            'total': float(self.total),
            'paye': float(self.paye),
            'reste': float(self.reste),
            'debut': str(self.debut),
            'fin': str(self.fin),
            'pourcentage': float((self.paye/self.total)*100)
        }


    def pourcentage(self):
        p = (self.paye/self.total)*100
        return p
        
        
    def getColor(self):
        pour = self.pourcentage()
        if pour < 50:
            return 'red'
        return 'green'
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, idclient):
        return cls.query.filter_by(idclient=idclient).all()