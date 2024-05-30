from projet import app
from projet.db import db
from flask import render_template, redirect, request, session, url_for
from projet.services.importcsv import import_first, import_second


@app.route('/to_import_first', methods=['GET'])
def to_import_first():
    return render_template('admin/import-premier.html')

@app.route('/to_import_second', methods=['GET'])
def to_import_second():
    return render_template('admin/import-deux.html')




@app.route('/importer_prem', methods=['POST'])
def importer_prem():
    fichier_mt = request.files['maison_travaux']
    fichier_devis = request.files['devis']
    
    if fichier_mt.filename == '' or fichier_devis.filename == '':
        return {'error': 'Les noms de fichiers ne peuvent pas être vides.'}, 400
    
    chemin_fichier_mt = fichier_mt.filename
    chemin_fichier_devis = fichier_devis.filename
    
    fichier_mt.save(chemin_fichier_mt)
    fichier_devis.save(chemin_fichier_devis)
    import_first(chemin_fichier_mt, chemin_fichier_devis)
    
    return redirect(url_for('dashboard'))




@app.route('/importer_sec', methods=['POST'])
def importer_sec():
    if 'paiement' not in request.files:
        return 'Aucun fichier envoyé'
    
    fichier_paiement = request.files['paiement']
    
    if fichier_paiement.filename == '':
        return {'error': 'Le nom de fichiers ne peuvent pas être vides.'}, 400
    chemin_fichier_paiement = fichier_paiement.filename
    fichier_paiement.save(chemin_fichier_paiement)
    import_second(chemin_fichier_paiement)
    return redirect(url_for('dashboard'))
    