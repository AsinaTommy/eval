from projet import app
from flask import render_template, redirect, request, session, url_for
from projet.services.importe import *
from projet.models.admin import *
from projet.services.numero import verifier_numero_telephone


@app.route('/', methods = ['GET'])
def index():
    return redirect(url_for('login_client'))


@app.route('/login-client', methods = ['GET'])
def login_client():
    return render_template("login-client.html")


@app.route('/login-admin', methods = ['GET'])
def login_admin():
    return render_template("login-admin.html")


@app.route('/check-client', methods = ['POST'])
def check_client():
    num = request.form['numero']
    if(verifier_numero_telephone(num)):
        session['user'] = {'numero': num, 'roles': ['CLIENT']}
    else:
        message= "veuillez verifier votre format de numero"
        return render_template("errorpage.html",message=message)
    return render_template("main/client.html")



@app.route('/check-admin', methods = ['POST'])
def connexadmin():
    email = request.form['email']
    password = request.form['password']
    
    admin = Admin.query.filter_by(email=email).one_or_none()
    if not admin or not admin.check_password(password):
        session['user'] = {'numero': 'tout', 'roles': ['ADMIN']}
        message= "Mot de passe ou email invalid"
        return render_template("errorpage.html",message=message)
    return render_template("main/admin.html")