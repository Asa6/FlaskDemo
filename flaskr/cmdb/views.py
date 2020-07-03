from flask_restful import Resource
from flask import request


class CMDBList(Resource):
    def __init__(self):
        self.ret = {"code": None, "msg": None, "data": None}

    def get(self):
        try:
            json_data = request.get_json()

            self.ret['code'] = '200'
            self.ret['msg'] = '资产列表查询成功'
            self.ret['data'] = json_data
        except Exception as e:
            self.ret["code"] = "500"
            self.ret["msg"] = e

        return self.ret

    def post(self):
        return {'Method': 'POST'}


class CMDB(Resource):
    def get(self, id):
        return {'Method': 'GET', 'Class': 'CMDB', 'id': id}

    def put(self, id):
        return { 'Method': 'PUT', 'id': id }

    def delete(self, id):
        return { 'Method': 'PUT', 'id': id }
