# imports
import sqlite3
from flask import Flask, g

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
import archie.views

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# aspects
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()
