from utilities.env_config import get_config_with_default
from flask import (
    Blueprint, jsonify
)

bp = Blueprint('base', __name__, url_prefix='/')


@bp.route('/ready')
def health():
    return jsonify(success=True)


@bp.route('/liveness')
def liveness():
    return jsonify(success=True)


@bp.route('/info')
def info():
    return jsonify(pod_name=get_config_with_default('POD_NAME', 'POD_NAME env var not set'),
                   version=get_config_with_default('VERSION', 'VERSION env var not set'))
