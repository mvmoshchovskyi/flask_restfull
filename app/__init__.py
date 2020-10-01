from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt import JWT

from config import DevConfig


app = Flask(__name__)
app.config.from_object(DevConfig)


db = SQLAlchemy(app)
api = Api(app)
bcrypt = Bcrypt()

from security import identity, authenticate
JWT(app, authenticate, identity)


from .resources import UserResource

api.add_resource(UserResource, '/', '/<int:id>')
