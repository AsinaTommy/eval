from projet.db import db

class V_board(db.Model):
    # pass
    __tablename__='v_board'
    __table_args__ = {'info': dict(is_view=True)}
    
    total = db.Column(db.Numeric(10,2), primary_key=True)
    paye = db.Column(db.Numeric(10,2))
    reste = db.Column(db.Numeric(10,2))
    
    