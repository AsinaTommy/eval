from projet.db import db

def delete_all_data(*models):
    try:
        for model in models:
            db.session.query(model).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(str(e))
        
        
# def delete        
        
