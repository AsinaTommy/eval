from projet import app
from flask import render_template, redirect, url_for, jsonify
from projet.models.pdf import Pdf
from projet.services.importe import *
from io import BytesIO
from projet.models.trails import Trail
from geoalchemy2 import WKTElement
from shapely.geometry import Polygon
from shapely.wkt import dumps



@app.route('/importer_donnees', methods=['GET'])
def importer_donnees():
    cond, donnee = import_fichier('D:/eval/projet-flask-eval/donnees-import.xlsx')
    if cond:
        return {'message':'le fichier a ete importe'}
    else:
        return {'errors':donnee}
    

@app.route('/test_pdf', methods=['GET'])
def export_pdf():
    html = render_template('client/monpdf.html')
    pdf = Pdf().render_pdf(html)

    # Convertir les données PDF de bytes en StringIO pour Flask
    pdf_io = BytesIO(pdf)
    headers = {
        'content-type': 'application.pdf',
        'content-disposition': 'inline  ; filename=certificate.pdf'}
    return pdf_io, 200, headers

@app.route('/map', methods=['GET'])
def map():
    return render_template("client/map.html")


@app.route('/add_point', methods=['GET'])
def add_point():
    coordinates = [
    (-10.0, 45.0),
    (-10.0, 55.0),
    (-25.0, 55.0),
    (-25.0, 45.0)
]

    polygon = Polygon(coordinates)
    wkt_polygon = dumps(polygon)
    new_trail = Trail(name='madagascar', difficulty=15, area=WKTElement(wkt_polygon, srid=4326))
    new_trail.save_to_db()
    return redirect(url_for('map'))

@app.route('/api/trails')
def get_trails():
    trails = Trail.find_all()
    return jsonify({
        'type': 'FeatureCollection',
        'features': [trail.to_geojson() for trail in trails]
    })

