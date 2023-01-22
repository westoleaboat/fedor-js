from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_moment import Moment
from datetime import datetime
from db import notes
import uuid
from flask_smorest import Api
from resources.notes import blp as NoteBlueprint


def create_app():

    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    moment = Moment(app)

    load_dotenv()
    app.config['SECRET_KEY'] = 'super-hard to guess string'
    app.config["PROPAGATE_EXCEPTIONS"] = True

    app.config["API_TITLE"] = "Notes REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)

    api.register_blueprint(NoteBlueprint)

    class NameForm(FlaskForm):
        name = StringField('Write your note')  # , validators=[DataRequired()])
        submit = SubmitField('Submit')

    # your URL routes are in reources/notes.py

    return app
