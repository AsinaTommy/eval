#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

from flask_sqlalchemy import SQLAlchemy
from projet import app

db = SQLAlchemy()

def delete_all_data(model):
    try:
        db.session.query(model).delete()
        db.session.commit()
        print(f"Toutes les données de la table {model.__tablename__} ont été supprimées avec succès.")
    except Exception as e:
        db.session.rollback()
        print(f"Une erreur s'est produite lors de la suppression des données de la table {model.__tablename__}: {e}")