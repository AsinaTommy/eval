from projet import app
from projet.db import db
from flask import render_template, redirect, request, session, url_for

from projet.models.detailsdevis import DetailDevis
from projet.models.devis import Devis
from projet.models.finition import Finition
from projet.models.maison import Maison
from projet.models.maisontravaux import MaisonTravaux
from projet.models.paiement import Paiement
from projet.models.travaux import Travaux
from projet.models.v_detailsdevis import V_detailsdevise
from projet.models.v_board import V_board
from projet.models.histogramme import Histogramme
from projet.models.v_devis import V_devis
from projet.services.formattage import formatone
from projet.services.trim import delete_all_data

@app.route('/liste-devisad', methods = ['GET'])
def list_devisad():
    return render_template("admin/devis-list.html")


@app.route('/dashboard/', defaults={'annee': None}, methods=['GET'])
@app.route('/dashboard/<int:annee>/', methods=['GET'])
def dashboard(annee):
    donnee = V_board.query.all()
    
    donnee[0].total = formatone(donnee[0].total)
    donnee[0].paye = formatone(donnee[0].paye)
    donnee[0].reste = formatone(donnee[0].reste)
    
    # Si aucune année n'est fournie dans l'URL, utilisez None
    if annee is not None:
        histo = Histogramme.query.filter(Histogramme.annee == annee).all()
        # Formatez les données dans le format attendu (une liste de listes)
        data2 = [[item.libelle, item.montant] for item in histo]
    else:
        data2 = []
   
    return render_template("admin/dashboard.html", data=donnee, data2=data2)


@app.route('/details-dev/<int:id>', methods=['GET'])
def details(id):
    donne = V_detailsdevise.query.filter(V_detailsdevise.iddevis==id)
    # for d in donne:
    #     print(d.iddevis, d.libelle, d.pu)
    return render_template("admin/details-devis.html", data = donne)



@app.route('/get-histo/<int:annee>', methods=['GET'])
def gethistor(annee):
    donnee = V_board.query.all()
    
    colonne_tri = getattr(Histogramme, "moi")
    histo = Histogramme.query.filter(Histogramme.annee == annee).order_by(colonne_tri.asc()).all()
    # Formatez les données dans le format attendu (une liste de listes)
    data2 = [[item.libelle[:4], item.montant] for item in histo]
    return data2


@app.route('/get-travaux', methods=['GET'])
def list_travaux():
    data = Travaux.find_all()
    return render_template("admin/liste-travaux.html", travaux = data)



@app.route('/get-all-devis', methods=['GET'])
def list_devis_all():
    data = V_devis.find_all()
    
    return render_template("admin/liste-devis.html", data = data)


@app.route('/get-finition', methods=['GET'])
def list_finition():
    data = Finition.find_all()
    return render_template("admin/liste-finition.html", finition = data)
   

@app.route('/update-travaux/<int:id>', methods=['GET'])
def update_travaux(id):
    data = Travaux.find_by_id(id)
    return render_template("admin/update-travaux.html", travaux = data)

@app.route('/update-finition/<int:id>', methods=['GET'])
def update_finition(id):
    data = Finition.find_by_id(id)
    return render_template("admin/update-finition.html",finition = data)


@app.route('/change-finition/<int:id>', methods=['POST'])
def change_finition(id):
    num = request.form['libelle']
    augmenttation = request.form['augmentation']
    data = Finition.find_by_id(id)
    data.augmentation = augmenttation
    data.libelle=num
    data.save_to_db()
    return redirect(url_for('list_finition'))



@app.route('/change-travaux/<int:id>', methods=['POST'])
def change_travaux(id):
    num = request.form['libelle']
    unite = request.form['unite']
    pu = request.form['pu']
    code = request.form['code']
    data = Travaux.find_by_id(id)
    data.libelle = num
    data.unite = unite
    data.pu = pu
    data.code = code
    data.save_to_db()
    return redirect(url_for('list_travaux'))



@app.route('/delete-all', methods=['GET'])
def delete_all():
    delete_all_data(DetailDevis,Paiement,Devis,MaisonTravaux,Travaux,Finition,Maison)
    return redirect(url_for('dashboard'))



