from flask_restful import Resource


class User(Resource):
    def get(self):
        return {'Method': 'GET', 'Class': 'User'}

    def post(self):
        return {'Method': 'POST'}
