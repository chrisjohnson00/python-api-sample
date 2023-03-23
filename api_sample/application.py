from flask import (
    Blueprint, jsonify
)

bp = Blueprint('app', __name__, url_prefix='/api')


@bp.route('/v1/users')
def index():
    return jsonify(users=[{'firstname': 'Sam', 'lastname': 'Ample', 'id': 12345},
                          {'firstname': 'Ample', 'lastname': 'Sam', 'id': 54321}])


@bp.route('/ready')
def health():
    return jsonify(success=True)


@bp.route('/liveness')
def liveness():
    return jsonify(success=True)
