# imports
import sqlite3
from flask import Flask, redirect, url_for, g, render_template

# config
DATABASE = '/tmp/archie.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
PROVIDER_SITE_ROUTE = 'http://archie-antonine.org'

# startup and utils
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# aspects
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

# routes
@app.route('/')
def index():
    return redirect(url_for('pois'))

@app.route('/pois')
def pois():
    return render_template('pois.xml')

# boot
if __name__ == '__main__':
    app.debug = True
    app.run()
