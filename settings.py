from os import getenv, urandom
from dotenv import load_dotenv
# -------------------------- #
from main import api


load_dotenv()

SECRET_KEY = urandom(32) # key => b'+\xf0l\x17+\x971\x1f\xda\xe7\x ...
DEBUG = True # if production mode => debug equal to false


# Get token from enviroment
ASSISTANT_TOKEN = getenv("ASSISTANT_TOKEN")
DIRECTOR_TOKEN = getenv("DIRECTOR_TOKEN")
PRODUCER_TOKEN = getenv("PRODUCER_TOKEN")

api.debug = DEBUG
api.secret_key = SECRET_KEY

