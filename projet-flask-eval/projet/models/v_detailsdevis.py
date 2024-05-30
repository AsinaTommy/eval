from projet.db import db

class V_detailsdevise(db.Model):
    pass
    __tablename__ = 'v_detailsdevise'
    __table_args__ = {'info': dict(is_view=True)}

    ligne = db.Column(db.Integer, primary_key =True)
    iddevis = db.Column(db.Integer)
    quantite = db.Column(db.Integer)
    idtravaux = db.Column(db.Integer)
    libelle = db.Column(db.String)
    pu = db.Column(db.Float)
    unite = db.Column(db.String)
    valeur = db.Column(db.Float)
    

    def json(self):
        return {
            'iddevis': self.iddevis,
            'quantite': self.quantite,
            'idtravaux': self.idtravaux,
            'libelle': self.libelle,
            'pu': self.pu,
            'unite': self.unite,
            'valeur': self.valeur
        }
