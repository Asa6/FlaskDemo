from flask_restful import Resource


class UserList(Resource):
    def __init__(self):
        self.ret = {"code": None, "msg": None, "data": None}

    def get(self):
        try:
            # json_data = request.get_json()


            self.ret['code'] = '200'
            self.ret['msg'] = '用户列表查询成功'
            self.ret['data'] = json_data
        except Exception as e:
            self.ret["code"] = "500"
            self.ret["msg"] = e

        return self.ret

    def post(self):
        return self.ret


class User(Resource):
    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
