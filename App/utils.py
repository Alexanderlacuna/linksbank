import jwt
from functools import wraps
from flask import jsonify,request



def generate_jwt_token():
    pass


def validate_token():
    pass


def token_required(func):
    @wraps
    def inner_function(*args, **kwargs):
        token = request.args.get("token")
        if token is None:
            return jsonify({"message": "Error occurred"}), 401

        try:
            # need to fetch secret key
            current_user = jwt.decode(token, "secret")

        except Exception as e:
            return jsonify({"message": "authentication failed"})
        return func(current_user, *args, **kwargs)
