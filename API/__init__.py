from flask import Flask
import firebase_admin
from firebase_admin import credentials, initialize_app



cred = credentials.Certificate("key.json")
default_app = firebase_admin.initialize_app(cred)



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']=''

    from app import app

    app.register_blueprint(app,url_prefix='/account')
    app.register_blueprint(app,url_prefix='/favorites')

    return app
