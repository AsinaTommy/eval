from projet.db import db
from projet import app

postgresql = {'host': 'localhost',
         'user': 'asina',
         'passwd': 'asina12',
         'db': 'eval'}

postgresqlConfig = "postgresql+psycopg2://{}:{}@{}/{}".format(postgresql['user'], postgresql['passwd'], postgresql['host'], postgresql['db'])

app.config['SQLALCHEMY_DATABASE_URI'] = postgresqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def create_tables():
    db.create_all()

with app.app_context():
    app.before_request_funcs = [(None, create_tables())]
    pass
    