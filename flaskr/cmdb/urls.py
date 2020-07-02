from flask_restful import Api
from .views import CMDB, CMDBList
from flask import Blueprint


cmdb_bp = Blueprint('cmdb', __name__)
api = Api(cmdb_bp)


api.add_resource(CMDBList, '/v1/cmdbs')
api.add_resource(CMDB, '/v1/cmdbs/<id>')

