from flask import Blueprint

movie = Blueprint('movies_views', __name__)

from . import movies
