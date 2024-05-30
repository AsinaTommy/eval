import pandas as pd

from projet.models import Importe
from projet.services.erreur import *
from projet.db import delete_all_data

def importer(fichier):
    donnees = pd.read_excel(fichier)
    tableau_donnees = []
    for index, ligne in donnees.iterrows():
        ligne_donnees = {}
        for nom_colonne, valeur in ligne.items():
            ligne_donnees[nom_colonne] = valeur
        tableau_donnees.append(ligne_donnees)
    return tableau_donnees          
            
def insert_import(fichier):
    donnees = importer(fichier)
    for donnee in donnees:
        ns = donnee['NumSeance']
        film = donnee['Film'].strip()
        categorie = donnee['Categorie'].strip()
        salle = donnee['Salle'].strip()
        date = donnee['Date']
        heure = donnee['Heure']
        importe_instance = Importe(ns, film, categorie, salle, date, heure)
        importe_instance.save_to_db()
    
    
def import_fichier(fichier):
    delete_all_data(Importe)
    insert_import(fichier)
    tab = Importe.find_all()
    tab_error = chekerror(tab)
    if(len(tab_error) == 0):
        # miantso fonction miinserer par table
        Importe.insert_from_import()
        return True, None
    else:
        return False, [t.json() for t in tab_error]
    
    
    
# importer('D:\eval\projet-flask-eval\donnees-import.xlsx')    