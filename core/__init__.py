from flask import Flask, make_response, jsonify
from flask_caching import Cache

''' This is for starting our App. We get the APP_SETTINGS from the configuration file in the root folder '''
app = Flask(__name__)
app.config.from_object('config.Config')

''' Caching for our flask app '''
cache = Cache(app)
from core import routes


''' Custome error messages '''
from core.models import ValidationError


''' The following methods  are friendly looking messages for invalid requests. '''

@app.errorhandler(ValidationError)
def bad_request(e):
    response = jsonify({'status': 400, 'error': 'bad request',
                        'message': e.args[0]})
    response.status_code = 400
    return response


@app.errorhandler(400)
def page_not_found(e):
    return make_response(jsonify({'error': 'Bad Request', 'message': e.args[0]}), 400)


@app.errorhandler(404)
def page_not_found(e):
    return make_response(jsonify({'error': 'Requested page is not available', 'message': e.args[0]}), 404)


@app.errorhandler(403)
def page_not_found(e):
    return make_response(jsonify({'error': 'Access to the requested resource is forbidden', 'message': e.args[0]}), 403)


@app.errorhandler(410)
def page_not_found(e):
    return make_response(jsonify({'error': 'Access to the target resource is no longer available at the origin server', 'message': e.args[0]}), 410)
