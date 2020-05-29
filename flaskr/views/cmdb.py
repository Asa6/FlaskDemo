from flask import Blueprint
bp = Blueprint('cmdb', __name__)


@bp.route('/api/v1/cmdbs')
def index():
    return 'Hello, cmdb!'
