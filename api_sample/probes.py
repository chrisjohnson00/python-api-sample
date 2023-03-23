from flask import (
    Blueprint, jsonify
)

bp = Blueprint('probes', __name__, url_prefix='/')


@bp.route('/ready')
def health():
    return jsonify(success=True)


@bp.route('/liveness')
def liveness():
    return jsonify(success=True)
