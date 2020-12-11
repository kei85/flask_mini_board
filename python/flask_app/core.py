from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_app.Config')

    return app

app = create_app()
db = SQLAlchemy(app)
ma = Marshmallow(app)
