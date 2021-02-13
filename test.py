import unittest
from os import getenv, path
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
# ------------------ #
from main import api
from settings import ASSISTANT_TOKEN, DIRECTOR_TOKEN, PRODUCER_TOKEN
from database.models import Actor, Movie


# Define Auth Headers:
assistant_header = {
    "Authorization": f"Bearer {ASSISTANT_TOKEN}"
}

director_header = {
    "Authorization": f"Bearer {DIRECTOR_TOKEN}"
}

producer_header = {
    "Authorization": f"Bearer {PRODUCER_TOKEN}"
}


# Test Case
class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.api = api
        self.client = self.api.test_client
        self.project_dir = path.dirname(path.abspath(__file__))

        self.actor_data = {
            "name": 'new_artist',
            "age": 99,
            "gender": 'artist_gender'

        }

        self.actor_patch_data = {
            "name": 'new_artist_1',
            "age": 99,
            "gender": 'artist_gender'
        }

        self.movie_data = {
            "title": "New Movie",
            "release_date": "20.09.1999"
        }

        self.movie_patch_data = {
            "title": "New Movie Patch!",
            "release_date": "20.09.1999"
        }

    def tearDown(self):
        pass

    def test_server(self):
        response = self.client().get('/')
        status = response.status_code
        self.assertEqual(status, 200)

    # TEST: send request without authorization header

    # Checking Actor Endpoints without auth header
    def test_get_actors_401(self):
        response = self.client().get('/api/actors')
        status = response.status_code
        self.assertEqual(status, 401)

    def test_post_actor_401(self):
        response = self.client().post('/api/actors/add', json=self.actor_data)
        status = response.status_code
        self.assertEqual(status, 401)

    def test_patch_actor_401(self):
        response = self.client().patch('/api/actor/1', json=self.actor_patch_data)
        status = response.status_code
        self.assertEqual(status, 401)

    def test_delete_actor_401(self):
        response = self.client().delete('/api/actor/1')
        status = response.status_code
        self.assertEqual(status, 401)

    # Checking Movie Endpoints without auth header

    def test_get_movies_401(self):
        response = self.client().get('/api/movies')
        status = response.status_code
        self.assertEqual(status, 401)

    def test_post_movie_401(self):
        response = self.client().post('/api/movies/add', json=self.movie_data)
        status = response.status_code
        self.assertEqual(status, 401)

    def test_patch_movie_401(self):
        response = self.client().patch('/api/movie/1', json=self.movie_patch_data)
        status = response.status_code
        self.assertEqual(status, 401)

    def test_delete_movie_401(self):
        response = self.client().delete('/api/movie/1')
        status = response.status_code
        self.assertEqual(status, 401)

    # Checking all endpoints with valid headers

    # Check Actor endpoints
    def test_get_actors(self):
        response = self.client().get('/api/actors', headers=producer_header)
        status = response.status_code
        self.assertEqual(status, 200)

    def test_post_actor(self):
        response = self.client().post(
            '/api/actors/add', json=self.actor_data, headers=producer_header)
        status = response.status_code
        self.assertEqual(status, 200)

    def test_patch_actor(self):
        data = Actor.query.first()
        response = self.client().patch(
            f'/api/actor/{data.id}', json=self.actor_patch_data, headers=producer_header)
        status = response.status_code
        self.assertEqual(status, 200)

    def test_delete_actor(self):
        data = Actor.query.first()
        response = self.client().delete(
            f'/api/actor/{data.id}', headers=producer_header)
        status = response.status_code
        self.assertEqual(status, 200)

    # Checking Movie Endpoints for correct!
    def test_get_movies(self):
        response = self.client().get('/api/movies', headers=producer_header)
        status = response.status_code
        self.assertEqual(status, 200)

    def test_post_movie(self):
        response = self.client().post(
            '/api/movies/add', json=self.movie_data, headers=producer_header)
        status = response.status_code
        self.assertEqual(status, 200)

    def test_patch_movie(self):
        data = Movie.query.first()
        response = self.client().patch(
            f'/api/movie/{data.id}', json=self.movie_patch_data, headers=producer_header)
        status = response.status_code
        self.assertEqual(status, 200)

    def test_delete_movie(self):
        data = Movie.query.first()
        response = self.client().delete(
            f'/api/movie/{data.id}', headers=producer_header)
        status = response.status_code
        self.assertEqual(status, 200)

    # Test endpoints without required permissions

    def test_post_actor_without_permissions(self):
        response = self.client().post(
            '/api/actors/add', json=self.actor_data, headers=assistant_header)
        status = response.status_code
        self.assertEqual(status, 401)

    def test_patch_actor_without_permissions(self):
        data = Actor.query.first()
        response = self.client().patch(
            f'/api/actor/{data.id}', json=self.actor_patch_data, headers=assistant_header)
        status = response.status_code
        self.assertEqual(status, 401)

    def test_delete_actor_without_permissions(self):
        data = Actor.query.first()
        response = self.client().delete(
            f'/api/actor/{data.id}', headers=assistant_header)
        status = response.status_code
        self.assertEqual(status, 401)

    def test_post_movie_without_permissions(self):
        response = self.client().post(
            '/api/movies/add', json=self.movie_data, headers=assistant_header)
        status = response.status_code
        self.assertEqual(status, 401)

    def test_patch_movie_without_permissions(self):
        data = Movie.query.first()
        response = self.client().patch(
            f'/api/movie/{data.id}', json=self.movie_patch_data, headers=assistant_header)
        status = response.status_code
        self.assertEqual(status, 401)

    def test_delete_movie_without_permissions(self):
        data = Movie.query.first()
        response = self.client().delete(
            f'/api/movie/{data.id}', headers=assistant_header)
        status = response.status_code
        self.assertEqual(status, 401)

    # Send bad Request: Checking for [400]

    # try post actor with bad request data

    def test_post_actor_400(self):
        response = self.client().post(
            '/api/actors/add', json={"ame": '', "question": 10}, headers=producer_header)
        status = response.status_code
        self.assertEqual(status, 400)

    # try patch actor with bad request data
    def test_patch_actor_400(self):
        data = Actor.query.first()
        response = self.client().patch(
            f'/api/actor/{data.id}', json={"nam": '', "question": 10}, headers=producer_header)
        status = response.status_code
        self.assertEqual(status, 400)

    # try post new movie with bad request data
    def test_post_movie_400(self):
        response = self.client().post(
            '/api/movies/add', json={"title": '', "question": 10}, headers=producer_header)
        status = response.status_code
        self.assertEqual(status, 400)

    # try patch movie with bad request data
    def test_patch_movie_400(self):
        data = Movie.query.first()
        response = self.client().patch(
            f'/api/movie/{data.id}', json={"title": '', "question": 10}, headers=producer_header)
        status = response.status_code
        self.assertEqual(status, 400)

    # Test for 404:
    
    # Try to delete 404 actor
    def test_delete_actor(self):
        response = self.client().delete(
            f'/api/actor/9999999999', headers=producer_header)
        status = response.status_code
        self.assertEqual(status, 404)

    # Try to delete 404 movie
    def test_delete_movie(self):
        response = self.client().delete(
            f'/api/movie/999999999', headers=producer_header)
        status = response.status_code
        self.assertEqual(status, 404)

if __name__ == "__main__":
    unittest.main()