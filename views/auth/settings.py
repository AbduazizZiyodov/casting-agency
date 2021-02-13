from os import getenv
from dotenv import load_dotenv

load_dotenv() # activate dotenv module

# define auth service variables
AUTH0_DOMAIN = getenv("AUTH0_DOMAIN")
API_AUDIENCE = getenv("API_AUDIENCE")
ALGORITHMS = ["RS256"]