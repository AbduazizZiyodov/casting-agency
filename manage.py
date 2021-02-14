import unittest
from flask import Flask
from os import system
from flask_script import Manager
from logging import Formatter, FileHandler, INFO
from flask_migrate import Migrate, MigrateCommand
# --------------------------------------------- #
from main import api, db
from helpers import db_prepare


migrate = Migrate(api, db)

manager = Manager(api)
manager.add_command('db', MigrateCommand)

file_handler = FileHandler('error.log')
file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
)

api.logger.setLevel(INFO)
file_handler.setLevel(INFO)
api.logger.addHandler(file_handler)

@manager.command
def prepare():
    db_prepare()

@manager.command
def runserver(): 
    api.run()

@manager.command
def test():
    system("python test.py")

if __name__ == '__main__':
    manager.run()