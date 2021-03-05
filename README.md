# Casting Agency 😁

>Udacity Full Stack Web Developer Nanodegree: Final Project🥳 !
## Intro

>**NOTE**: API hosted in heroku 🚀: abduaziz-casting-agency.herokuapp.com 


> ⚠️ User data for testing this project:
>*   producer@mail.com
>*   director@mail.com
>*   assistant@mail.com
>-   Password: $Udacity007

The Casting Agency API supports a basic agency by allowing users manage their movies and actors. 
There are 3 different user roles👥:
 - Casting Assistant
 - Casting Director
 - Casting Producer

Role based permissions:
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
    - `read:actors`
    - `read:movies`
    - `add:actors`
    - `delete:actors`
    - `update:actors`
    - `update:movies`
    - `delete:actors`
    - `delete:movies`

## Getting Started 😉

Requirements:
- Python 3 🐍 (https://www.python.org/)
- Database(https://www.postgresql.org/, pgadmin optional) 💾
- PIP packages 📦
- CURL for testing this API 💣
>[!] Postman (recommended) 🚀


First steeps -> clone this repo:

```bash
$ git clone https://github.com/AbduazizZiyodov/casting-agency.git
$ cd casting-agency/
```
Create and activate your virtual enviroment:

```bash
$ python -m venv env
$ source env/scripts/activate
```

Install all required pip packages:

```bash
$ pip install -r requirements.txt
```

Change some config vars in your enviroment file:

```bash
$ touch .env #create dotenv file
$ nano .env
--------------------
DATABASE_URL = "url"
--------------------
```

Before running server, prepare your database.

```bash
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```

Run:

```bash
$ python wsgi.py # or
$ python manage.py runserver 
```

You can get **JWT** tokens by navigate this page:
``` 
https://abduaziz.us.auth0.com/authorize?audience=casting_id&response_type=token&client_id=37TyLsTlvmZdXN5XL4SIjZp7drUTsw7h&redirect_uri=http://127.0.0.1:5000/login-results
```

>NOTE: you can check your JWT token by navigating this page: jwt.io
> ![CURL](/screenshots/jwtio.PNG)

# Testing

### 1. First method: CURL

**NOTE** You can find more commands from API reference :)

Open your terminal and type `curl`:
![CURL](/screenshots/curl.PNG)

And run testing commands in API reference.

For example:
![CURL_EX](/screenshots/curl_eg.PNG)

### 2. Second method: Unittest

**NOTE** I have written my own test case :)

In project directory you should define JWT tokens in file `settings.py`:
![JWT](/screenshots/settings.PNG)

After defining tokens, you can run testing process using unittest:

![TEST](/screenshots/test_result.PNG)

### 3. Third method: Postman

**NOTE:** I have written my own postman collection for this API. You can use it for testing :)

> Register and Install postman: https://www.postman.com/downloads/

Open your Postman, import my collection in your dashboard:

![IMPORT](/screenshots/import.PNG)

Prepare your enviroment. Define api host and JWT tokens from Globals tab:

![GLOBALS](/screenshots/globals.PNG)

After defining, you can open your runner and drag your collection:

![RUNNER](/screenshots/runner.PNG)

Test this API using Postman runner:

![POSTMAN](/screenshots/postman.PNG)

🎉 Yes! 

```python
>>> test.is_success()
[out] True
```

## API reference

In this API authentication is **required**. This API uses JWT token for authentication.

### Endpoints

**Actor** endpoints:
*   `api/actors` - methods: [GET]. **Get** all actor data.
*   `api/actor/<id>` - methods: [GET,PATCH,DELETE].
    *   **GET** - get actor data by id.
    *   **PATCH** - update actor.
    *   **DELETE** - delete actor.
*   `api/actors/add` - methods: [POST]. Add new Actor

<hr>

**Movie** endpoints:
*   `api/movies` - methods: [GET]. Get all actor data.
*   `api/movie/<id>` - methods: [GET,PATCH,DELETE].
    *   **GET** - get movie data by id.
    *   **PATCH** - update movie.
    *   **DELETE** - delete movier.
*   `api/movies/add` - methods: [POST]. Add new Movie

### Error handling & error messages

Type of error messages is **JSON** (json response)

*   **400** - bad request error.
*   **401** - all auth errors (+ with description).
*   **404** - not found error.

>Sample Response:
>```json
>{
>   "success": False,
>   "error": 404,
>   "message": "Not found"
>}
>```

### `GET` - Actor endpoints

##### 1. `GET` ACTORS

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

##### 2. `GET` ACTOR

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

##### 1. `GET` MOVIES

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

##### 2. `GET` MOVIE

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

### `DELETE` - Actor endpoints

* Methods: **DELETE**
* URL: `/api/actor/<id>`
* Permission: `delete:actors`

>[!] Request body is not required

Sample request using CURL:

```bash
curl --location --request DELETE \
'https://abduaziz-casting-agency.herokuapp.com/api/actor/1' \
--header 'Authorization: Bearer <token>'
```

Sample request using Python:

```python
import requests

url = "https://abduaziz-casting-agency.herokuapp.com/api/actor/1"

payload={}
headers = {
  'Authorization': 'Bearer <token>'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

Response:

*   Success(200):

```json
{
    "success": True,
    "id": 1
}
```

*   Not Found(404):

```json
{
    "success": False,
    "error": 404,
    "message": "Not found"
}
```

#### Author:

Abduaziz Ziyodov - Backend Developer (python).

><i>26.02.2021<i>