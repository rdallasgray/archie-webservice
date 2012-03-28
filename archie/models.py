from archie import db

class Poi(db.Model):
    __tablename__ = 'pois'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))
    type = db.Column(db.String(255))
    co_ordinates = db.Column(db.String(255))
    thumbnail = db.Column(db.String(255))
    hi_res_image_url = db.Column(db.String(255))
    marker_icon_url = db.Column(db.String(255))

    def __repr__(self):
        return '<Poi %s>' % (self.name)

class Attachment(db.Model):
    __tablename__ = 'attachments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    type = db.Column(db.String(255))
    url = db.Column(db.String(255))
    thumbnail = db.Column(db.String(255))

    def __repr__(self):
        return '<Attachment %s>' % (self.name)

class Target(db.Model):
    __tablename__ = 'targets'
    id = db.Column(db.Integer, primary_key=True)
    poi_id = db.Column(db.Integer)
    action = db.Column(db.String(255))
    ip = db.Column(db.String(255))
    user_agent = db.Column(db.String(255))
    device = db.Column(db.String(255))
    os = db.Column(db.String(255))
    action_time = db.Column(db.String(255))
    latitude = db.Column(db.String(255))
    longitude = db.Column(db.String(255))
    
    
    def __repr__(self):
        return '<Target %d>' % (self.id)

