from flask import Blueprint

web = Blueprint('web', __name__)


@web.route('/hello')
def hello():
    headers = {
        'content-type': 'application/json'
    }
    return '{"A": 12}', 400, headers
