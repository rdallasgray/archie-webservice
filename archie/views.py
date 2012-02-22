from archie import app, models
from flask import make_response, redirect, url_for, render_template

# routes
@app.route('/')
def index():
    return redirect(url_for('pois'))
    
@app.route('/pois')
def pois():
    resp = make_response(render_template('pois.xml', pois=models.Poi.query.all()))
    resp.headers['Content-type'] = 'text/xml'
    return resp
