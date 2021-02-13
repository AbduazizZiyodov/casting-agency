from flask import Blueprint, jsonify, abort, request
# ------------------------------------------------ #
from views.movie import movie
from database.models import Actor, Movie
from ..auth import requires_auth, AuthError


@movie.route('/movies', methods=['GET'])
@requires_auth('read:movies')
def get_all_movies(token):

    data = Movie.query.all()

    if not data:
        return jsonify({
            "message": "No Movies Found",
            "number_of_movies": len(data),
            "success": False
        }), 404

    response = {
        "success": True,
        "number_of_movies": len(data),
        "movies": [
            movie.format() for movie in data
        ]
    }

    return jsonify(response), 200


@movie.route('/movies/add', methods=['POST'])
@requires_auth('add:movies')
def add_new_movie(token):
    data = request.get_json()

    if len(data['title']) == 0 or len(data['release_date']) == 0:
        abort(400)

    movie = Movie.query.filter_by(title=data['title']).first()

    if movie:
        return jsonify({
            "mesage":"This film is already available",
            "success": False
        })

    new_movie = Movie(
        title=data['title'],
        release_date=data['release_date']
    )

    new_movie.insert()

    response = {
        "success": True,
        "actor": new_movie.format()
    }

    return jsonify(response), 200


@movie.route('/movie/<int:id>', methods=['PATCH'])
@requires_auth('update:movies')
def update_movie(token,id):

    movie = Movie.query.get(id)

    if not movie:
        abort(404)

    data = request.get_json()

    if len(data['title']) == 0 or len(data['release_date']) == 0:
        abort(400)

    try:
        if data['title'] and data['release_date']:
            movie.title = data['title']
            movie.release_date = data['release_date']

    except:
        abort(400)

    movie.update()

    response = {
        'success': True,
        'message': "Movie Updated!",
        'movie': movie.format()
    }

    return jsonify(response), 200


@movie.route('/movie/<int:id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movie(token,id):
    if not id:
        abort(404)

    data = Movie.query.get(id)
    if not data:
        abort(404)

    try:
        data.delete()

    except Exception as e:
        print(e)
        abort(422)

    response = {
        "success": True,
        "id": id
    }

    return jsonify(response), 200