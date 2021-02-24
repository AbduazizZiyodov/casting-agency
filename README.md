# Casting Agency

>Udacity Full Stack Web Developer Nanodegree: Final Project!
## Intro

The Casting Agency API supports a basic agency by allowing users manage their movies and actors. 
There are 3 different user roles:
 - Casting Assistant
 - Casting Director
 - Casting Producer

And role based permissions:
- Casting Assistant:
    - `read:actors`
    - `read:movies`
- Casting Director:
    - `read:actors`
    - `read:movies`
    - `add:actors`
    - `delete:actors`
    - `update:actors`
    - `update:movies`
- Casting Producer:
    **All Permissions Director + Add or Delete Movie.**

## Getting Started

Requirements:
- Python3
- Database(sqlite or postgresql)
- Terminal(+curl)
- PIP packages
- Postman(optional)

Clone this repo:

```bash
$ git clone https://github.com/AbduazizZiyodov/casting-agency.git
$ cd casting-agency/
```
Create and Activate virtual enviroment:

```bash
$ python -m venv env
$ source env/scripts/activate
```

Install all required packages:

```bash
$ pip install -r requirements.txt
```
Change some configuration vars:

```bash
$ touch .env #create dotenv file
$ nano .env
------------------
DATABASE_URL = "url"
-------------------
```

Running development server. Before running server, prepare your database.

```bash
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
# run server:
$ python wsgi.py #or
$ python manage.py runserver 
```

You can get JWT tokens by navigate this page: 
https://abduaziz.us.auth0.com/authorize?audience=casting_id&response_type=token&client_id=37TyLsTlvmZdXN5XL4SIjZp7drUTsw7h&redirect_uri=http://127.0.0.1:5000/login-results


## API reference

In this API authentication is **required**. This API uses JWT token for authentication.

### Endpoints

**Actor** endpoints:
*   `api/actors` - methods: [GET]. Get all actor data.
*   `api/actor/<id>` - methods: [GET,PATCH,DELETE].
    *   GET - get actor data by id.
    *   PATCH - update actor.
    *   DELETE - delete actor.
*   `api/actors/add` - methods: [POST]. Add new Actor

<hr>

**Movie** endpoints:
*   `api/movies` - methods: [GET]. Get all actor data.
*   `api/movie/<id>` - methods: [GET,PATCH,DELETE].
    *   GET - get movie data by id.
    *   PATCH - update movie.
    *   DELETE - delete movier.
*   `api/movies/add` - methods: [POST]. Add new Movie

### API Error handling

*   400 - bad request error.
*   401 - all auth errors (+ with description).
*   404 - not found error.

>Sample Response:
>```json
>{
>   "success": False,
>   "error": 404,
>   "message": "Not found"
>}
>```

### `GET` - Actor endpoints

##### 1. GET ACTORS

* Methods: **GET**
* URL: `/api/actors`
* Permission: `read:actors`

Sample Request using CURL:

```bash
curl --location --request GET \
'https://abduaziz-casting-agency.herokuapp.com/api/actors' \
--header 'Authorization: Bearer <token>'
```

Sample Request using Python:

```python
import requests

url = "https://abduaziz-casting-agency.herokuapp.com/api/actors"

payload={}
headers = {
  'Authorization': 'Bearer <token>'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

Response:

*   Success(200):

```json

{
        "success": True,
        "actors": [
            {
                "id": "number",
                "name": "actor_name",
                "gender": "actor_gender",
                "age": "actor_age"  
            },
            {
                "id": "number2",
                "name": "actor_name2",
                "gender": "actor_gender2",
                "age": "actor_age2"  
            }
            
        ]
}

```
*   Not Found(404)

```json
{
    "message": "No Actors Found",
    "number_of_actors": 0,
    "success": False
}
```

##### 2. GET ACTOR

* Methods: **GET**
* URL: `/api/actor/<id>`
* Permission: `read:actors`

Sample Request using CURL:

```bash
curl --location --request GET \
'https://abduaziz-casting-agency.herokuapp.com/api/actor/<id>' \
--header 'Authorization: Bearer <token>'
```

Sample Request using Python:

```python
import requests

url = "https://abduaziz-casting-agency.herokuapp.com/api/actor/<id>"

payload={}
headers = {
  'Authorization': 'Bearer <token>'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

Response:

*   Success(200):

```json

{
    "id": "number",
    "name": "actor_name",
    "gender": "actor_gender",
    "age": "actor_age"  
}

```
*   Not Found(404):

```json
{
    "message": "No Actor Found",
    "success": False
}
```