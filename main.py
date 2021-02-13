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

api.register_blueprint(actor, url_prefix='/api')
api.register_blueprint(movie, url_prefix='/api')

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
    
@api.errorhandler(AuthError)
def auth_error(AuthError):
    return (jsonify(
        {
            "error": AuthError.status_code,
            "message": AuthError.error["message"],
            "success": False,
        }
    ), AuthError.status_code,)

@api.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request"}), 400

@api.errorhandler(403)
def forbidden(error):
    return jsonify({
        "success": False,
        "error": 403,
        "message": "Forbidden"}), 403

@api.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not found"}), 404

@api.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": "Method Not Allowed"}), 405

@api.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unprocessable"}), 422

@api.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal Server Error"}), 500

@api.errorhandler(502)
def bad_gateway(error):
    return jsonify({
        "success": False,
        "error": 502,
        "message": "Bad Gateway"}), 502