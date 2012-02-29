from archie import db
from archie.models import Poi, Attachment

def begin():
    db.drop_all()
    db.create_all()
    p = Poi('test', 'a test poi')
    db.session.add(p)
    db.session.commit()
