import os
import json
from flask import request
from functools import wraps
from jose import jwt
from urllib.request import urlopen
# ---------------------------------------- #
from .settings import ALGORITHMS, API_AUDIENCE, AUTH0_DOMAIN


JSON_URL = f'https://{AUTH0_DOMAIN}/.well-known/jwks.json'


"""
GUIDE https://auth0.com/docs/quickstart/backend/python/01-authorization
"""
# AuthError Exception
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# Auth Header
def get_token_auth_header():
    # Get Authorization from request header
    header = request.headers.get('Authorization', None)
    # If header not found
    if header is None:
        raise AuthError({
            'code': 401,
            'message': 'Authorization not in header'
        }, 401)

    # Place keyword & token  in result(result is array)
    result = header.split('Bearer ')
    # request header must be two parts
    if len(result) != 2:
        raise AuthError({
            'code': 401,
            'message': 'Authorization header is invalid. Bearer token not found'
        }, 401)
    # define our token
    token = result[1]

    if not token:
        raise AuthError({
            'code': 401,
            'message': 'Authorization header is invalid. Bearer token is empty'
        }, 401)

    return token

'''
@TODO implement check_permissions(permission, payload) method
    @INPUTS
        permission: string permission (i.e. 'post:drink')
        payload: decoded jwt payload
    it should raise an AuthError if permissions are not included in the payload
        !!NOTE check your RBAC settings in Auth0
    it should raise an AuthError if the requested permission
    string is not in the payload permissions array
    return true otherwise
'''
# Function for checking permission from payload data
def check_permissions(permission, payload):
    # define permissions from payload data
    permissions = payload.get('permissions', None)
    # if permission not found
    if permissions is None:
        raise AuthError({
            'code': 401,
            'message': 'Any permissions not in token'
        }, 401)
    # if permission in payload, but this permission is not suitable for doing smth.   
    if permission not in permissions:
        raise AuthError({
            'code': 401,
            'message': 'Permission not found this action'
        }, 401)

'''
@TODO implement verify_decode_jwt(token) method
    @INPUTS
        token: a json web token (string)
    it should be an Auth0 token with key id (kid)
    it should verify the token using Auth0 /.well-known/jwks.json
    it should decode the payload from the token
    it should validate the claims
    return the decoded payload
    !!NOTE urlopen has a common certificate error described
'''
# function for decode jwt token (+verify)
def verify_decode_jwt(token):
    # get key from our auth0 server
    json_url = urlopen(JSON_URL)
    jwks = json.loads(json_url.read())

    try:
        # try to get header and define it
        unverified_header = jwt.get_unverified_header(token)
    # JWT ERROR exception
    except jwt.JWTError:
        raise AuthError({
            'code': 401,
            'message': 'Error decoding token headers.'
        }, 401)
    # define empty rsa key
    rsa_key = {}

    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 401,
            'message': 'Authorization malformed.'
        }, 401)

    for key in jwks['keys']:
        # all is match => we should build rsa key
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }

    if rsa_key:
        # if we have rsa key:
        try:
            # decode it
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload
        # Expired exception
        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 401,
                'message': 'Token expired.'
            }, 401)
        # JWT claims error
        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 401,
                'message': 'Incorrect claims. Please, check the audience and issuer.'
            }, 401)
        # JWT parsing error
        except Exception:
            raise AuthError({
                'code': 401,
                'message': 'Unable to parse authentication token.'
            }, 401)

    raise AuthError({
        'code': 401,
        'message': 'Unable to find the appropriate key.'
    }, 401)


# Build own decorator
# default => permission is None
def requires_auth(permission=''):
    def requires_auth_decorator(f):
        # using functool wraps
        @wraps(f)
        def wrapper(*args, **kwargs):
            # get auth token from own helper function
            token = get_token_auth_header()
            # verify this token and get payload
            payload = verify_decode_jwt(token)
            # check permission by comparing permission and payload
            check_permissions(permission, payload)
            # return it!
            return f(payload, *args, **kwargs)
        # return our wrapper function
        return wrapper
    # finally we can return our decorator
    return requires_auth_decorator
# This decorator is usable  :) 