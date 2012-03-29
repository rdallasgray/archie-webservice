from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy
import archie.config

# startup and utils
app = Flask(__name__)
app.config.from_object(archie.config.TestingConfig)
db = SQLAlchemy(app)
import archie.views
import archie.install

# recreate the db from scratch
archie.install.begin()

