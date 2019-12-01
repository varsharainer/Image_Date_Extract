"""
Import all necessary packages/libraries
"""

from flask import Flask
import flask_compress
from flask_cors import CORS
from OpenSSL import SSL
from flask_sslify import SSLify

from Scripts.Utils import utility
from Scripts.date_extract_main import api_main



"""Declaring API:::"""
project_app = Flask(__name__)

"""Compressing the Response (Archiving)"""
flask_compress.Compress(project_app)

"""Connecting all services (for multiple API services"""
project_app.register_blueprint(api_main)

CORS(project_app, resources={r'/*': {'origins': '*'}})


if __name__ == '__main__':
    """Running main services::"""
    project_app.run(host=utility.config["settings"]["ip"], port=utility.config["settings"]["port"], debug=True, threaded=True, use_reloader=False)
