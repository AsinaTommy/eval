from projet import app
from flask import render_template, redirect, request, session, url_for

from projet.annotation.authentication import auth
from projet.models.v_devis import V_devis

@app.route('/getdata', methods = ['POST'])
def getdata():
    numero = session['user']['numero']
    form = request.form
    size = int(form.get('size'))
    page = int(form.get('page'))
    tri_col = form.get('tri')
     
    if tri_col == 'null' or tri_col=='undefined':
        tri_col = 'iddevis'
        
    colonne_tri = getattr(V_devis, tri_col)
    requete = V_devis.query.filter(V_devis.idclient==numero)
    requete = requete.order_by(colonne_tri.asc()).paginate(page=page, per_page=size)
     
    return {'data': [req.json() for req in requete]}, 200 


@app.route('/getdevisad', methods = ['POST'])
def getdevisad():
    # numero = session['user']['numero']
    
    form = request.form
    size = int(form.get('size'))
    page = int(form.get('page'))
    tri_col = form.get('tri')
     
    if tri_col == 'null' or tri_col=='undefined':
        tri_col = 'iddevis'
        
    colonne_tri = getattr(V_devis, tri_col)
    requete = V_devis.query
    requete = requete.order_by(colonne_tri.asc()).paginate(page=page, per_page=size)
     
    return {'data': [req.json() for req in requete]}, 200 

