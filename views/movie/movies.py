from flask import Blueprint, jsonify, abort, request
# ------------------------------------------------ #
from views.movie import movie
from database.models import Actor, Movie
from ..auth import requires_auth, AuthError


def validate(title, date):
    try:
        if len(title) > 1 and len(date) > 3:
            return True

        else:
            return False
    except TypeError:
        return False

@movie.route('/movies', methods=['GET'])
@requires_auth('read:movies')
def get_all_movies(token):

    data = Movie.query.all()

    if not data:
        return jsonify({
            "message": "No Movies Found",
            "number_of_movies": len(data),
            "success": False
        }), 200

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

    if data is None:
        abort(400)

    try:
        title, date = data["title"], data["release_date"]

    except KeyError:
        abort(400)

    if validate(title, date):
        movie = Movie.query.filter_by(title=title).first()

        if movie:
            return jsonify({
                "mesage": "This film is already available",
                "success": False
            })
        new_movie = Movie(
            title=title,
            release_date=date
        )

        new_movie.insert()

        response = {
            "success": True,
            "actor": new_movie.format()
        }

        return jsonify(response), 200

    return abort(400)


@movie.route('/movie/<int:id>', methods=['PATCH'])
@requires_auth('update:movies')
def update_movie(token, id):

    movie = Movie.query.get(id)

    if not movie:
        abort(404)

    data = request.get_json()

    if data is None:
        abort(400)

    try:
        title, date = data["title"], data["release_date"]
    except KeyError:
        abort(400)

    if validate(title, date):

        movie.title = title
        movie.release_date = date

        try:
            movie.update()
            
        except:
            abort(422)

        response = {
            'success': True,
            'message': "Movie Updated!",
            'movie': movie.format()
        }

        return jsonify(response), 200

    return abort(400)


@movie.route('/movie/<int:id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movie(token, id):
    if not id:
        abort(404)

    data = Movie.query.get(id)

    if data is None:
        abort(404)

    try:
        data.delete()

    except:
        abort(422)

    response = {
        "success": True,
        "id": id
    }

    return jsonify(response), 200
