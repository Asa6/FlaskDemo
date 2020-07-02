from flask_restful import Resource


class CMDBList(Resource):
    def get(self):
        return {'Method': 'GET', 'Class': 'CMDBList'}

    def post(self):
        return {'Method': 'POST'}


class CMDB(Resource):
    def get(self, id):
        return {'Method': 'GET', 'Class': 'CMDB', 'id': id}

    def put(self, id):
        return { 'Method': 'PUT', 'id': id }

    def delete(self, id):
        return { 'Method': 'PUT', 'id': id }
