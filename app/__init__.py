__author__ = 'Azzssss'

from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object("config")

db = MogoEngine(app)

from app import views, models