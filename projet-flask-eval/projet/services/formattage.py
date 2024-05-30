nombre = 10000.20
nombre_formate = "{:,}".format(nombre)
print(nombre_formate)

nombre = 1000.050
# Utilisation de l'espace comme séparateur
nombre_formate_avec_espace = "{:,.0f}".format(nombre).replace(',', ' ')
# Utilisation du point comme séparateur
nombre_formate_avec_point = "{:,.0f}".format(nombre).replace(',', '.')
print(nombre_formate_avec_espace)  # Affiche : 1 000 000
print(nombre_formate_avec_point)   # Affiche : 1.000.000
 # Affiche : 1,000,000

nombre_decimal = 1234567.89
# Utilisation de la virgule comme séparateur et affichage de deux chiffres après la virgule
nombre_formate_virgule = "{:,.2f}".format(nombre_decimal).replace(',', ' ')
# Utilisation du point comme séparateur et affichage de deux chiffres après la virgule
nombre_formate_point = "{:,.2f}".format(nombre_decimal).replace(',', '.')
print(nombre_formate_virgule)  # Affiche : 1 234 567,89
print(nombre_formate_point)    # Affiche : 1.234.567,89


nombre_decimal = 1234567.89
# Utilisation de la virgule comme séparateur et affichage de deux chiffres après la virgule
nombre_formate_virgule = f"{nombre_decimal:,.2f}".replace(',', ' ')
# Utilisation du point comme séparateur et affichage de deux chiffres après la virgule
nombre_formate_point = f"{nombre_decimal:,.2f}".replace(',', '.')
print(nombre_formate_virgule)  # Affiche : 1 234 567,89
print(nombre_formate_point)    # Affiche : 1.234.567,89


from datetime import datetime
import locale

def formatone(nb):
    return f"{nb:,.2f}".replace(',', ' ')



def formate_date(dat):
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
    date = datetime(dat)
    date_formatee = date.strftime("%A %d %B %Y")
    return date_formatee