import re

def verifier_numero_telephone(numero):
    if len(numero) != 10:
        return False
    
    if not numero.isdigit():
        return False
    
    prefixes_valides = ['032', '033', '034', '038']
    if not numero.startswith(tuple(prefixes_valides)):
        return False
    
    return True


def verifier_numero_telephone2(numero):
    # Supprimer les espaces et les tirets éventuels
    numero = numero.replace(' ', '').replace('-', '')
    
    # Vérifier si le numéro contient 10 chiffres ou commence par +261 suivis de 9 chiffres
    if not (len(numero) == 10 or (numero.startswith('+261') and len(numero) == 13)):
        return False
    
    # Vérifier si tous les caractères restants sont des chiffres
    if not numero[1:].isdigit():
        return False
    
    # Vérifier si le numéro commence par l'un des préfixes valides pour Madagascar
    prefixes_valides = ['032', '033', '034', '038']
    if not numero.startswith(('0' + prefixe for prefixe in prefixes_valides)) and not numero.startswith('+261'):
        return False
    
    # Si toutes les conditions sont remplies, le numéro est valide
    return True


