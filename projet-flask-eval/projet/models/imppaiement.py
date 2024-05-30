from projet.db import db

class ImportPaiement(db.Model):
    __tablename__ = 'importpaiement'
   
    id = db.Column(db.Integer, primary_key=True)
    ref_devis = db.Column(db.String)
    ref_paiement = db.Column(db.String)
    date_paiement = db.Column(db.Date)
    montant = db.Column(db.Float)

    def __init__(self, ref_devis, ref_paiement, date_paiement, montant):
        self.ref_devis = ref_devis
        self.ref_paiement = ref_paiement
        self.date_paiement = date_paiement
        self.montant = montant
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_ref(cls, ref):
        return cls.query.filter_by(ref_paiement=ref).first()

    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
