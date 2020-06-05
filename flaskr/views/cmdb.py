from flask import (
    Blueprint, request
)
bp = Blueprint('cmdb', __name__)


@bp.route('/api/v1/cmdbs', methods=['GET', 'POST'])
def index():

    print(request.method)

    # 获取GET请求方法
    if request.method == 'GET':

        # 获取get请求参数：ip
        ip = request.args.get('ip')
        print('ip:', ip)

        return 'CMDB, GET!'


    # 获取POST请求方法
    if request.method == 'POST':

        # 获取body内容
        post_body = request.form
        print('post_body:', post_body)


        return 'CMDB, POST!'
