from flask import Blueprint


actor = Blueprint('artist_views', __name__)

from . import actors