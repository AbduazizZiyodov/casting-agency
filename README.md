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
``` 
https://abduaziz.us.auth0.com/authorize?audience=casting_id&response_type=token&client_id=37TyLsTlvmZdXN5XL4SIjZp7drUTsw7h&redirect_uri=http://127.0.0.1:5000/login-results
```

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
### `GET` - Movie endpoints

##### 1. GET MOVIES

* Methods: **GET**
* URL: `/api/movies`
* Permission: `read:movies`

Sample Request using CURL:

```bash
curl --location --request GET \
'https://abduaziz-casting-agency.herokuapp.com/api/movies' \
--header 'Authorization: Bearer <token>'
```

Sample Request using Python:

```python
import requests

url = "https://abduaziz-casting-agency.herokuapp.com/api/movies"

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
        "number_of_movies": 2,
        "movies": [
            {
                "id": "number",
                "title": "movie title",
                "release_date": "1999"
            },
            {
                "id": "number",
                "title": "movie title",
                "release_date": "1999"
            },
            
        ]
}

```
*   Not Found(404)

```json
{
    "message": "No Movies Found",
    "number_of_movies": 0,
    "success": False
}
```

##### 2. GET MOVIE

* Methods: **GET**
* URL: `/api/movie/<id>`
* Permission: `read:movies`

Sample Request using CURL:

```bash
curl --location --request GET \
'https://abduaziz-casting-agency.herokuapp.com/api/movie/<id>' \
--header 'Authorization: Bearer <token>'
```

Sample Request using Python:

```python
import requests

url = "https://abduaziz-casting-agency.herokuapp.com/api/movie/<id>"

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
    "title": "movie title",
    "release_date": "1999"
}

```
*   Not Found(404)

```json
{
    "message": "No Movie Found",
    "success": False
}
```


### `POST` - Actor endpoints

* Methods: **POST**
* URL: `/api/actors`
* Permission: `add:actors`

>[!] Required Request Body

Request body structure:

```json
{
    "name": str,
    "age": int,
    "gender": "men" or "women"
}
```

Sample Request using Curl:

```bash
curl --location --request POST \
'https://abduaziz-casting-agency.herokuapp.com/api/actors/add' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data-raw '{
	"name": "New Actor Name",
	"age": 99,
	"gender": "Men"
}'
```

Sample Request using Python:

```python
import requests

url = "https://abduaziz-casting-agency.herokuapp.com/api/actors/add"

payload="{\r\n\t\"name\": \"New Actor Name\",\r\n\t\"age\": 99,\r\n\t\"gender\": \"Men\"\r\n}"
headers = {
  'Authorization': 'Bearer <token>',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```

Response:

*   Success(200):

```json

{
    "success": True,
    "actor": {
        "name": "actor_name",
        "gender": "actor_gender",
        "age": "actor_age"  
    }
}

```
*   Bad Request(400)

```json
{
    "success": False,
    "error": 400,
    "message": "Bad Request"
}
```

### `POST` - Movie endpoints

* Methods: **POST**
* URL: `/api/movies`
* Permission: `add:movies`

>[!] Required Request Body

Request body structure:

```json
{
    "title": str,
    "release_date": int,
}
```

Sample Request using Curl:

```bash
curl --location --request POST \
'https://abduaziz-casting-agency.herokuapp.com/api/movies/add' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data-raw '{
	"title": "New Super Film",
	"release_date": "1999"
}'
```

Sample Request using Python:

```python
import requests

url = "https://abduaziz-casting-agency.herokuapp.com/api/movies/add"

payload="{\r\n\t\"title\": \"New Super Film\",\r\n\t\"release_date\": \"1999\"\r\n}"
headers = {
  'Authorization': 'Bearer <token>',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


```

Response:

*   Success(200):

```json

{
    "success": True,
    "movie": {
        "title": "New Super Film",
        "release_date": "1999"
    }
}

```
*   Bad Request(400)

```json
{
    "success": False,
    "error": 400,
    "message": "Bad Request"
}
```

### `PATCH` - Actor endpoints

* Methods: **PATCH**
* URL: `/api/actor/<id>`
* Permission: `update:actors`

>[!] Required Request Body

Request body structure:

```json
{
    "name": str,
    "age": int,
    "gender": "men" or "women"
}
```

Sample Request using Curl:

```bash
curl --location --request PATCH \
'https://abduaziz-casting-agency.herokuapp.com/api/actor/<id>' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data-raw '{
	"name": "Updated Actor Data",
	"age":93,
	"gender":"Men"
}'
```

Sample Request using Python:

```python
import requests

url = "https://abduaziz-casting-agency.herokuapp.com/api/actor/<id>"

payload="{\r\n\t\"name\": \"Updated Actor Data\",\r\n\t\"age\":93,\r\n\t\"gender\":\"Men\"\r\n}"
headers = {
  'Authorization': 'Bearer <token>',
  'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
```
Response:

*   Success(200):

```json

{
    "success": True,
    "message": "Actor Updated!",
    "actor": {
        "name": "actor_name",
        "gender": "actor_gender",
        "age": "actor_age"  
    }
}

```
*   Bad Request(400)

```json
{
    "success": False,
    "error": 400,
    "message": "Bad Request"
}
```

### `PATCH` - Movie endpoints

* Methods: **PATCH**
* URL: `/api/movie/<id>`
* Permission: `update:movies`

>[!] Required Request Body

Request body structure:

```json
{
    "title": str,
    "release_date": int,
}
```

Sample Request using Curl:

```bash
curl --location --request PATCH \
'https://abduaziz-casting-agency.herokuapp.com/api/movie/<id>' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data-raw '{
	"title": "Updated Film",
	"release_date": "1999"
}'
```

Sample Request using Python:

```python
import requests

url = "https://abduaziz-casting-agency.herokuapp.com/api/movie/<id>"

payload="{\r\n\t\"title\": \"Updated Film\",\r\n\t\"release_date\": \"1999\"\r\n}"
headers = {
  'Authorization': 'Bearer <token>',
  'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)

```
Response:

*   Success(200):

```json

{
    "success": True,
    "message": "Movie Updated!",
    "movie": {
        "title": "Updated Film",
        "release_date": "1999"
    }   
}

```
*   Bad Request(400)

```json
{
    "success": False,
    "error": 400,
    "message": "Bad Request"
}
```