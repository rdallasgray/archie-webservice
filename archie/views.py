from archie import app
from flask import redirect, url_for, render_template

# routes
@app.route('/')
def index():
    return redirect(url_for('pois'))
    
@app.route('/pois')
def pois():
    return render_template('pois.xml')
