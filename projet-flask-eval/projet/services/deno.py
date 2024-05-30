from projet.db import db
from projet.models.travaux import Travaux
from projet.models.detailsdevis import DetailDevis
from datetime import datetime

def insert_detailsdevis(maisontravaux, iddevis):
    for maison in maisontravaux:
        travaux = Travaux.find_by_id(maison.idtravaux)
        detail = DetailDevis(iddevis,maison.idtravaux,maison.quantite,travaux.pu)
        
        
        detail.save_to_db()
        
def get_now():
    return datetime.now().date()        