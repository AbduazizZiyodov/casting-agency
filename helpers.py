from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#-------------------------------------#
from main import api, db
from database.models import Actor, Movie


def fill_database():
    actor_data_1  = Actor(name='new actor_1', age=99, gender="men")
    actor_data_2  = Actor(name='new actor_2', age=99, gender="men")
    movie_data_1  = Movie(title='forsaj 9', release_date="2021")
    movie_data_2  = Movie(title="forsaj 10", release_date="2022")

    all_data = [actor_data_1, actor_data_2, movie_data_1, movie_data_2]

    for data in all_data:
        data.insert()

def db_prepare():
    db.session.commit()
    db.drop_all()
    db.create_all()
