from flask import Blueprint
bp = Blueprint('usre', __name__)


@bp.route('/api/v1/users')
def index():
    return 'Hello, users!'
