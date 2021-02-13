from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    Column,
    Integer,
    String,
    Date
)
from os import getenv


db = SQLAlchemy()


"""
Movie
A Movie database model
"""
class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    release_date = Column(String, nullable=False)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def __str__(self):
        return self.title

    '''
    insert()
        insert a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            data = Object(title= ...)
            data.insert()
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    update()
        updates a model
        the model must exist in the database
        EXAMPLE
            data = Object.query.filter(Object.id == id).one_or_none()
            data.title = 'smth new'
            data.update()
    '''

    def update(self):
        db.session.commit()

    '''
    delete()
        deletes model from database
        the model must exist in the database
        EXAMPLE
            data = Object(title=...)
            data.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
        }


"""
Actor
A Actor database model
"""
class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return self.name

        '''
    insert()
        insert a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            data = Object(name= ...)
            data.insert()
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    update()
        updates a model
        the model must exist in the database
        EXAMPLE
            data = Object.query.filter(Object.id == id).one_or_none()
            data.name = 'smth new'
            data.update()
    '''
    def update(self):
        db.session.commit()

    '''
    delete()
        deletes model from database
        the model must exist in the database
        EXAMPLE
            data = Object.query.filter(Object.id == id).one_or_none()
            data.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }