from flask_restful import Resource


class CMDB(Resource):
    def get(self):
        return {'Method': 'GET', 'Class': 'CMDB'}

    def post(self):
        return {'Method': 'POST'}
