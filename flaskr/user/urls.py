from flask_restful import Api
from .views import UserList, User
from flask import Blueprint


user_bp = Blueprint('user', __name__)
api = Api(user_bp)


api.add_resource(UserList, '/v1/users/')
api.add_resource(User, '/v1/users/<id>')

