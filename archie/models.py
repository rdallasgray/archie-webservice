from archie import db

class Poi(db.Model):
    __tablename__ = 'pois'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))
    thumbnail = db.Column(db.String(255))
    hi_res_image_url = db.Column(db.String(255))
    marker_icon_url = db.Column(db.String(255))
    co_ordinates = db.Column(db.String(255))

    def __init__(self, name=None, description=None, thumbnail=None,
                 hi_res_image_url=None, marker_icon_url=None, co_ordinates=None):
        self.name = name
        self.description = description
        self.thumbnail = thumbnail
        self.hi_res_image_url = hi_res_image_url
        self.marker_icon_url = marker_icon_url
        self.co_ordinates = co_ordinates

    def __repr__(self):
        return '<Poi %r>' % (self.name)

class Attachment(db.Model):
    __tablename__ = 'attachments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    type = db.Column(db.String(255))
    url = db.Column(db.String(255))
    thumbnail = db.Column(db.String(255))

    def __init__(self, name=None, type=None, url=None, thumbnail=None):
        self.name = name
        self.type = type
        self.url = url
        self.thumbnail = thumbnail

    def __repr__(self):
        return '<Poi %r>' % (self.name)

