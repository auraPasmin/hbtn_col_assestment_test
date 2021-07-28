from flask import Blueprint

app_routes = Blueprint('app_routes', __name__, url_prefix='/api/v1')

from api.v1.routes.orders import *