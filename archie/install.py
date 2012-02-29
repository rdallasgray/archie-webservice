from archie import db
from archie.models import Poi, Attachment
from archie.data import data

def begin():
    db.drop_all()
    db.create_all()
    for poi_data in data:
        p = Poi(**poi_data)
        db.session.add(p)
    db.session.commit()
