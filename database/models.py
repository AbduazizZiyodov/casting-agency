from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    Column,
    Integer,
    String,
    Date
)
from os import getenv


db = SQLAlchemy()