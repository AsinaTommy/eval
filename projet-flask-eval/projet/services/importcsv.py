import csv
from projet.models.paiement import Paiement
from sqlalchemy import text

from projet.db import delete_all_data,db
from projet.models.impdevis import ImportDevis
from projet.models.impmaisontravaux import ImportMaisonTravaux
from projet.models.imppaiement import ImportPaiement
from projet.services.erreur import chekerror
from datetime import datetime


def lire_file(fichier):
    donnees = []
    with open(fichier, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            donnees.append(row)
    return donnees


def insert_import_mt(fichier):
    donnees = lire_file(fichier)
    for donnee in donnees:
        tm = donnee['type_maison'].strip()
        desc = donnee['description'].strip()
        surface = donnee['surface']
        code = donnee['code_travaux'].strip()
        type = donnee['type_travaux'].strip()
        unite = donnee['unite'].strip()
        prix = donnee['prix_unitaire'].replace(',','.')
        quantite = donnee['quantite'].replace(',','.')
        duree = donnee['duree_travaux']
        rep = ImportMaisonTravaux(tm,desc,surface,code,type,unite,prix,quantite,duree)
        rep.save_to_db()
      

def insert_import_devis(fichier):
    donnees = lire_file(fichier)
    for donnee in donnees:
        client = donnee['client']
        ref_devis = donnee['ref_devis'].strip()
        type_maison = donnee['type_maison'].strip()
        finition = donnee['finition'].strip()
        taux_finition = donnee['taux_finition'].replace('%','').replace(',','.')
        date_devis = datetime.strptime(donnee['date_devis'], "%d/%m/%Y")
        date_debut = datetime.strptime(donnee['date_debut'], "%d/%m/%Y")
        lieu = donnee['lieu'].strip()
    
        rep = ImportDevis(client,ref_devis,type_maison,finition,taux_finition,date_devis,date_debut,lieu)
        rep.save_to_db()
    
    
def insert_import_paiement(fichier):
    donnees = lire_file(fichier)
    i =0
    ref = []
    for donnee in donnees:
        ref_devis = donnee['ref_devis'].strip()
        ref_paiement = donnee['ref_paiement'].strip()
        date_paiement = datetime.strptime(donnee['date_paiement'], "%d/%m/%Y")
        montant = donnee['montant']
        p = Paiement.query.filter(Paiement.reference==ref_paiement).all()

        i = i+1
        if len(p)<1 and (ref_paiement not in ref):
            rep = ImportPaiement(ref_devis,ref_paiement,date_paiement,montant)
            rep.save_to_db()
        if i > 0:
            ref.append(ref_paiement)
            

def insertionFinalData_first():
    db.session.execute(text("insert into maison (libelle, duree,surface,descriptions) select * from v_imp_maison"))
    db.session.execute(text("insert into travaux (libelle,unite,pu,code) select * from v_imp_travaux"))
    db.session.flush()
    db.session.execute(text("insert into maisontravaux (idmaison,idtravaux,quantite) select * from v_imp_maisontravaux"))
    db.session.execute(text("insert into finition (libelle, augmentation) select * from v_imp_finition"))
    db.session.execute(text("insert into devis (idmaison,idfinition,idclient,debuttravaux,augmentation,duree,datecreation,reference,lieu) select * from v_imp_devis"))
    db.session.execute(text("insert into detaildevis (iddevis,idtravaux,quantite,pu) select * from v_imp_detaildevis"))
    db.session.commit()

def insertionFinalData_second():
    db.session.execute(text("insert into paiement (iddevis,montant,dateheure,reference) select * from v_imp_paiement"))
    db.session.commit()
    
def import_first(fichier1,fichier2):
    delete_all_data(ImportMaisonTravaux)
    delete_all_data(ImportDevis)
    
    insert_import_mt(fichier1)
    insert_import_devis(fichier2)
    
    db.session.commit()
    
    #CheckError ty
    tab = ImportMaisonTravaux.find_all()
    # tab_error = chekerror(tab)
    tab2 = ImportDevis.find_all()
    # tab_error2 = chekerror(tab2)
    
    # if(len(tab_error) == 0 and len(tab_error2) == 0):
        # miantso fonction miinserer par table
    insertionFinalData_first()
    #     return True, None
    # else:
    #     return False, [t.json() for t in tab_error]


def import_second(fichier3):
    delete_all_data(ImportPaiement)
    insert_import_paiement(fichier3)
    
    #Checkerror
    # tab = ImportPaiement.find_all()
    # tab_error = chekerror(tab)
    
    
    # if(len(tab_error) == 0 ):
    #     # miantso fonction miinserer par table
    #     ImportPaiement.insert_from_import()
    insertionFinalData_second()
    #     return True, None
    # else:
    #     return False, [t.json() for t in tab_error]


