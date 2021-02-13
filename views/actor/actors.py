from flask import (
    Blueprint, 
    abort, 
    jsonify, 
    request
)    
# ---------------------------------------- #
from views.actor import actor
from database.models import Actor, Movie


@actor.route('/actors', methods=['GET'])
def get_all_actors(token):
    data = Actor.query.all()

    if not data:
        return jsonify({
            "message": "No Actors Found",
            "number_of_actors": len(data),
            "success": False
        }), 404

    response = {
        "success": True,
        "actors": [
            actor.format() for actor in data
        ]
    }

    return jsonify(response), 200

@actor.route('/actors/add', methods=['POST'])
def add_new_actor(token):
    data = request.get_json()


    if 'name' not in data or\
       'age' not in data or\
       'gender' not in data:
        abort(400)

    new_actor = Actor(
        name=data['name'],
        age=data['age'],
        gender=data['gender']
    )

    actor = Actor.query.filter_by(name=data["name"]).first()

    if actor:
        return jsonify({
            "mesage":"This actor is already available",
            "success": False
        })

    
    new_actor.insert()

    response = {
        "success": True,
        "actor": new_actor.format()
    }

    return jsonify(response), 200

@actor.route('/actor/<int:id>', methods=['PATCH'])
def update_actor(token,id):
    data = request.get_json()

    if not id:
        abort(404)

    actor = Actor.query.get(id)

    if not actor:
        abort(404)

    try:
        if data['name'] and data['age'] and data['gender']:
            actor.name, actor.age,  actor.gender = data['name'],\
                                    data['age'], data['gender']

    except Exception:
        abort(400)

    actor.update()

    response = {
        'success': True,
        'message': "Actor Updated!",
        'actor': actor.format()
    }
    return jsonify(response), 200


@actor.route('/actor/<int:id>', methods=['DELETE'])
def delete_actor(token,id):
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