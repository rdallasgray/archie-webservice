from archie import db
from archie.models import Poi, Attachment
from archie.data import data

def begin():
    db.drop_all()
    db.create_all()
    for poi_data in data:
        attachments = None
        if ("attachments" in poi_data):
            attachments = poi_data["attachments"]
            del poi_data["attachments"]
        p = Poi(**poi_data)
        db.session.add(p)
        if attachments:
            for attachment_data in attachments:
                p.attachments.append(Attachment(**attachment_data))
    db.session.commit()
