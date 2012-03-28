from archie import app, models, db
from flask import request, make_response, redirect, url_for, render_template

# routes
@app.route('/')
def index():
    return redirect(url_for('pois'))
    
@app.route('/pois')
def pois():
    resp = make_response(render_template('pois.xml', pois=models.Poi.query.all()))
    resp.headers['Content-type'] = 'text/xml'
    return resp

@app.route('/targets')
def targets():
    t = models.Target(**request.args.to_dict())
    db.session.add(t)
    db.session.commit()
    return make_response(t.__repr__())
