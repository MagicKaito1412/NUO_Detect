from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://u1:1@127.0.0.1:5432/nuo_detect?client_encoding=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

with app.app_context():
    db = SQLAlchemy(app)

import backend.db_module.controller
