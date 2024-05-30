from datetime import datetime
from io import BytesIO
import os


from projet import app
from flask import make_response, render_template, redirect, request, session, url_for
from projet.models.maison import Maison
from projet.models.finition import Finition
from projet.models.devis import Devis
from projet.models.maisontravaux import MaisonTravaux
from projet.models.paiement import Paiement
from projet.models.pdf import Pdf
from projet.models.v_detailsdevis import V_detailsdevise
from projet.models.v_devis import V_devis
from projet.services.deno import insert_detailsdevis,get_now
from projet.db import db


@app.route('/create-devis', methods = ['GET'])
def create_devis():
    data = []
    data2 = []
    for f in Maison.find_all():
        data.append(f.json())
    for p in Finition.find_all():  
        data2.append(p.json())
        
    return render_template("client/devis-create.html", maison = data, finition = data2)

@app.route('/liste-devis', methods = ['GET'])
def list_devis():
    return render_template("client/devis-list.html")


@app.route('/add-devis', methods=['POST'])
def ajout_devis():
    maison_selected = request.form['maisonradio']
    finition_selected = request.form['finitionradio']
    numero = session['user']['numero']
    date_debut = request.form['datedebut']
    duree =  Maison.find_by_id(maison_selected).duree
    augmentation = Finition.find_by_id(finition_selected).augmentation

    reference = "DEV001"
    lieu = request.form['lieu']
    
    devis = Devis(maison_selected,finition_selected,numero,date_debut,augmentation,duree, get_now(), reference, lieu)
    devis.save_to_db()
    db.session.flush()
    
    maison_travaux = MaisonTravaux.query.filter_by(idmaison=maison_selected).all()
    insert_detailsdevis(maison_travaux,devis.iddevis)
    db.session.commit()
    
    
    return  redirect('liste-devis')


@app.route('/paiement', methods=['GET'])
def create_paiement():
    data = []
    numero = session['user']['numero']
    for g in Devis.find_by_id(numero):
        data.append(g.json())
    return render_template("client/paiement.html", data = data)


@app.route('/add-paiement', methods=['POST'])
def add_paiement():
    iddevis = request.form['iddevis']
    montant = float(request.form['montant']) 
    date = request.form['date']
    
    devis = V_devis.query.filter(V_devis.iddevis==iddevis).first()
    if(montant>devis.reste):
        return {'error': 'montant invalid'}, 500
    
    p = Paiement(iddevis,montant,date,"P007")
    p.save_to_db()
    return {'message': 'montant bien valide'}, 200
    
    
@app.route('/export-pdf/<int:id>', methods = ['GET'])
def getpdf(id):
    data2 = Paiement.find_by_id(id)
    somme2 = 0
    for w2 in data2:
        somme2 += w2.montant
    
    
    data = V_detailsdevise.query.filter(V_detailsdevise.iddevis==id)
        
    data3 = V_devis.query.filter(V_devis.iddevis==id).first()
    somme = data3.total

    html = render_template('client/monpdf.html', data=data, somme = somme,data2=data2, somme2=somme2)    
    pdf = Pdf().render_pdf(html)

    pdf_io = BytesIO(pdf)
    headers = {
        'content-type': 'application.pdf',
        'content-disposition': 'inline  ; filename=devis.pdf'}
    return pdf_io, 200, headers
    
