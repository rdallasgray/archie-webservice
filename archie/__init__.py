from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy
import archie.config

# startup and utils
app = Flask(__name__)
app.config.from_object(archie.config.DevelopmentConfig)
db = SQLAlchemy(app)
import archie.views
import archie.install

archie.install.begin()

