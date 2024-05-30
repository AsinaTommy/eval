from projet.models.Erreur import Erreur

def checkLine(imp, tab_error, index):
    verifierSeance(imp.numseance,tab_error,index)


def verifierSeance(seance,tab_error,index):
    try:
        if(seance<20):
            tab_error.append(Erreur('valeur invalide: inferieure a 20', index+1, 1))
    except Exception as e:
            tab_error.append(Erreur(str(e), index+1, 1))
            
            
def chekerror(tab):
    tab_error = []
    for index,imp in enumerate(tab):
        checkLine(imp, tab_error, index)
    return tab_error    