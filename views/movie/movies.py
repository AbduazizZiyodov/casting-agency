from flask import Blueprint, jsonify, abort, request
# ------------------------------------------------ #
from views.movie import movie
from database.models import Actor, Movie
from ..auth import requires_auth, AuthError


# Simple Movie data Validator
def validate(title, date):
    try:
        if len(title) > 1 and len(date) > 3:
            return True

        else:
            return False
    except TypeError:
        return False

# Endpoint for get all movies
@movie.route('/movies', methods=['GET'])
@requires_auth('read:movies')
def get_all_movies(token):
    # fetch all data from database
    data = Movie.query.all()
    # if data is none
    if not data:
        return jsonify({
            "message": "No Movies Found",
            "number_of_movies": 0,
            "success": False
        }), 200
    # Build response data model
    response = {
        "success": True,
        "number_of_movies": len(data),
        "movies": [
            movie.format() for movie in data
        ]
    }
    # return response
    return jsonify(response), 200

# Endpoint for get movie data
@movie.route('/movie/<int:id>', methods=['GET'])
@requires_auth('read:movies')
def get_single_movie(token, id):
    # get movie by id
    data = Movie.query.get(id)
    # if movie is NONE return 404
    if data is None:
        return jsonify({
            "message": "No Movie Found",
            "success": False
        }), 404
    # else return movie data
    return jsonify(data.format()), 200

# Endpoint for adding new movies
@movie.route('/movies/add', methods=['POST'])
@requires_auth('add:movies')
def add_new_movie(token):
    # handle request data
    data = request.get_json()
    # if data is NONE
    if data is None:
        abort(400)
    # get data from request body
    try:
        title, date = data["title"], data["release_date"]
    # except return 400 error
    except KeyError:
        abort(400)
    # validate request data, if TRUE:
    if validate(title, date):
        # check for movie exist
        movie = Movie.query.filter_by(title=title).first()
        # if movie is exist return json response with message
        if movie:
            return jsonify({
                "mesage": "This film is already available",
                "success": False
            })
        # build new movie data
        new_movie = Movie(
            title=title,
            release_date=date
        )
        # add new movie
        new_movie.insert()
        # build response data
        response = {
            "success": True,
            "actor": new_movie.format()
        }
        # return response
        return jsonify(response), 200

    return abort(400)

# Endpoint for updating movie data
@movie.route('/movie/<int:id>', methods=['PATCH'])
@requires_auth('update:movies')
def update_movie(token, id):
    # get movie by id
    movie = Movie.query.get(id)
    # if movie is NONE return 404 error
    if not movie:
        abort(404)
    # handle request data
    data = request.get_json()
    # if request body is empty return 400 error
    if data is None:
        abort(400)
    # try to get data from request body
    try:
        title, date = data["title"], data["release_date"]
    # except return 400 error (bad request)
    except KeyError:
        abort(400)
    # validate request data, if TRUE:
    if validate(title, date):
        # update data
        movie.title = title
        movie.release_date = date
        # try to update movie
        try:
            movie.update()
        # except return 422 error
        except:
            abort(422)
        # build response data
        response = {
            'success': True,
            'message': "Movie Updated!",
            'movie': movie.format()
        }
        # return response
        return jsonify(response), 200

    return abort(400)

# Endpoint for deleting movies
@movie.route('/movie/<int:id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movie(token, id):
    # if is none return 404
    if not id:
        abort(404)
    # get movie by id
    data = Movie.query.get(id)
    # if request body is empty
    if data is None:
        abort(404)
    # delete movie
    try:
        data.delete()
    # if process was unsuccessful return 422 error
    except:
        abort(422)
    # build response data
    response = {
        "success": True,
        "id": id
    }
    # send response to user
    return jsonify(response), 200
