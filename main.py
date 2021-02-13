from flask import (
    Flask,
    abort,
    jsonify,
    url_for,
    redirect
)
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from logging import FileHandler, Formatter, INFO
# -------------------------------------------- #
from database.models import db, Actor, Movie
from views.actor import actor
from views.movie import movie
from views.auth import requires_auth, AuthError


api = Flask(__name__)


db.init_app(api)
db.app = api

api.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://abduaziz:2121@localhost:5432/casting"
api.debug = True

CORS(api,
     resources={r"/api/*": {"origins": "*"}}
     )


@api.after_request
def after_request(response):
    response.headers.add(
        "Access-Control-Allow-Headers",
        "Content-Type,Authorization")
    response.headers.add(
        "Access-Control-Allow-Methods",
        "GET,PATCH,POST,DELETE,OPTIONS")
    return response


@api.route('/')
def HomePage():
    return jsonify({
        "Agency_is_working": True
    })

@api.route('/docs')
def docs():
    return redirect(
        'https://abduaziz-ziyodov.gitbook.io/casting-agency/'
    )


