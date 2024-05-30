from projet.db import db
from geoalchemy2 import Geometry
from shapely.geometry import shape, mapping
from geoalchemy2.shape import to_shape

class Trail(db.Model):
    __tablename__ = 'trails'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    difficulty = db.Column(db.String(20))
    area = db.Column(Geometry('POLYGON'))  # Modifier le champ de géométrie pour stocker des polygones
    
    def __init__(self,name,difficulty,area) :
        self.name = name
        self.difficulty = difficulty
        self.area = area
        
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
    def to_geojson(self):
        shape_area = to_shape(self.area)
        return {
            'type': 'Feature',
            'geometry': mapping(shape_area),
            'properties': {
                'id': self.id,
                'name': self.name,
                'difficulty': self.difficulty
            }
        }