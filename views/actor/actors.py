from flask import (
    Blueprint,
    abort,
    jsonify,
    request
)
# --------------------------------------- #
from views.actor import actor
from database.models import Actor, Movie
from ..auth import requires_auth, AuthError


# number validator:
def is_num(n):
    try:
        if isinstance(n, int):
            return True
        if isinstance(n, float):
            return n.is_integer()

        return False

    except TypeError:
        return False    

# Simple validate function
def validate(name, age, gender):
    # define genders
    genders = ["men", "women"]
    try:
        # check data length and check gender & age
        if len(name) > 1 and \
                gender.lower() in genders and \
                is_num(age):
            return True
        else:
            return False
            
    except TypeError:
        return False

# Endpoint for get all actor data
@actor.route('/actors', methods=['GET'])
@requires_auth('read:actors')
def get_all_actors(token):
    # fetch all actor data from database
    data = Actor.query.all()

    # if data is NONE return json response with message
    if not data:
        return jsonify({
            "message": "No Actors Found",
            "number_of_actors": len(data),
            "success": False
        }), 200
    # build response data and add actors data
    
    response = {
        [actor.format() for actor in data]
    }
    # finaly return json response
    return jsonify(response), 200

# Endpoint for get actor data
@actor.route('/actor/<int:id>', methods = ['GET'])
@requires_auth('read:actors')
def get_single_actor(token, id):
    # fetch actor data by actor id
    data = Actor.query.get(id)
    # if actor is NONE return json response with message
    if data is None:
        return jsonify({
            "message": "No Actor Found",
            "success": False
        }),404 
    # else: return actor data
    return jsonify(data.format()),200

# Endpoint for adding new actors
@actor.route('/actors/add', methods=['POST'])
@requires_auth('add:actors')
def add_new_actor(token):
    # handler request data
    data = request.get_json()
    # if request body is empty return 400 error
    if data is None:
        abort(400)
    # try get data from request body
    try:
        name = data["name"]
        age = data["age"]
        gender = data["gender"]
    # if data handling is unsuccessful return 400 error
    except KeyError:
        abort(400)
    # validate request data, if TRUE:
    if validate(name, age, gender): 
        # build actor data
        new_actor = Actor(
            name=name,
            age=age,
            gender=gender.lower()
        )
        # check for: if actor exits!
        actor = Actor.query.filter_by(name=name).first()
        # if actor found, return json response with required message
        if actor:
            return jsonify({
                "mesage": "This actor is already available",
                "success": False
            }), 200
        # else: insert new actor to database
        try:
            new_actor.insert()
        # if this operation was unsuccessful: return 422 error
        except:
            abort(422)
        # build response data with actor data
        response = {
            "success": True,
            "actor": new_actor.format()
        }
        # return response
        return jsonify(response), 200

    return abort(400)

# Endpoint for updating actors data
@actor.route('/actor/<int:id>', methods=['PATCH'])
@requires_auth('update:actors')
def update_actor(token, id):
    # if is none
    if not id:
        abort(404)
    # handle request data
    data = request.get_json()
    # fetch actor from database by id
    actor = Actor.query.get(id)
    # if actor is none return 404 error
    if not actor:
        abort(404)
    # try get data from request body
    try:
        name = data['name']
        age = data['age']
        gender = data['gender']
    # except return bad request error
    except KeyError:
        abort(400)
    # validate request data, if TRUE:
    if validate(name, age, gender):
        # change data
        actor.name, actor.age, actor.gender = name, age, gender
        # try update actor data
        try:
            actor.update()
        # if process unsuccessful: return 422 error
        except:
            abort(422)
        # build response data
        response = {
            'success': True,
            'message': "Actor Updated!",
            'actor': actor.format()
        }
        # return response
        return jsonify(response), 200
    else:
        # if update process was unsuccessful: return 400 error
        return abort(400)

# Endpoint for deleting actors data
@actor.route('/actor/<int:id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actor(token, id):
    # if id is none return 404
    if not id:
        abort(404)
    # get actor data by id
    data = Actor.query.get(id)
    # if data not found return 404
    if data is None:
        abort(404)
    # try to delete actor data    
    try:
        data.delete()
    # except return 422 error
    except Exception:
        abort(422)
    # build response data
    response = {
        "success": True,
        "id": id
    }

    return jsonify(response), 200
