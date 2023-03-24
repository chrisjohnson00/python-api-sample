from utilities.env_config import get_config_with_default
from flask import (
    Blueprint, jsonify, make_response
)

bp = Blueprint('app', __name__, url_prefix='/api')


@bp.route('/v1/users')
def users():
    response = make_response(jsonify([{'firstname': 'Sam', 'lastname': 'Ample', 'id': 12345},
                                      {'firstname': 'Ample', 'lastname': 'Sam', 'id': 54321}]))
    response = set_default_response_headers(response)
    return response


@bp.route('/v1/comments')
def comments():
    response = make_response(jsonify([{'id': 1234, 'text': 'Foo the bar'}, {'id': 12345, 'text': 'Bar the foo'}]))
    response = set_default_response_headers(response)
    return response


def set_default_response_headers(response):
    response.headers['X-Pod-Name'] = get_config_with_default('POD_NAME', 'POD_NAME env var not set')
    response.headers['X-Version'] = get_config_with_default('VERSION', 'VERSION env var not set')
    return response
