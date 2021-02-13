from flask import (
    Blueprint,
    abort,
    jsonify,
    request
)
# ---------------------------------------- #
from views.actor import actor
from database.models import Actor, Movie
from ..auth import requires_auth, AuthError


# Request Data Validator:
def is_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()

    return False


def validate(name, age, gender):
    genders = ["men", "women"]

    if len(name) > 1 and \
            gender.lower() in genders and \
            is_num(age):
        return True
    else:
        return False


@actor.route('/actors', methods=['GET'])
@requires_auth('read:actors')
def get_all_actors(token):
    data = Actor.query.all()

    if not data:
        return jsonify({
            "message": "No Actors Found",
            "number_of_actors": len(data),
            "success": False
        }), 200

    response = {
        "success": True,
        "actors": [
            actor.format() for actor in data
        ]
    }

    return jsonify(response), 200


@actor.route('/actors/add', methods=['POST'])
@requires_auth('add:actors')
def add_new_actor(token):
    data = request.get_json()

    if data is None:
        abort(400)

    try:
        name = data["name"]
        age = data["age"]
        gender = data["gender"]

    except KeyError:
        abort(400)

    if validate(name, age, gender):

        new_actor = Actor(
            name=name,
            age=age,
            gender=gender.lower()
        )

        actor = Actor.query.filter_by(name=data["name"]).first()

        if actor:
            return jsonify({
                "mesage": "This actor is already available",
                "success": False
            }), 200

        try:
            new_actor.insert()
        except:
            abort(422)

        response = {
            "success": True,
            "actor": new_actor.format()
        }
        return jsonify(response), 200

    return abort(400)


@actor.route('/actor/<int:id>', methods=['PATCH'])
@requires_auth('update:actors')
def update_actor(token, id):
    if not id:
        abort(404)

    data = request.get_json()

    actor = Actor.query.get(id)

    if not actor:
        abort(404)

    try:
        name = data['name']
        age = data['age']
        gender = data['gender']

    except KeyError:
        abort(400)

    if validate(name, age, gender):

        actor.name, actor.age, actor.gender = name, age, gender

        try:
            actor.update()
        except:
            abort(422)

        response = {
            'success': True,
            'message': "Actor Updated!",
            'actor': actor.format()
        }
        return jsonify(response), 200

    else:
        return abort(400)


@actor.route('/actor/<int:id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actor(tokenm, id):
    if not id:
        abort(404)

    data = Actor.query.get(id)

    if not data:
        abort(404)
    try:
        data.delete()

    except Exception:
        abort(500)

    response = {
        "success": True,
        "id": id
    }

    return jsonify(response), 200
