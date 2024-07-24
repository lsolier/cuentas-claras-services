# core-apiselection/src/app.py

from src import create_app
from flask_cors import CORS

from src.api.views import HealthCheckView, ActividadesView, ViajeroView
from src.modelo.declarative_base import db
from flask import Blueprint
from flask_restful import Api
import logging
import os

# app setup
app = create_app('default')
app_context = app.app_context()
app_context.push()

# logging setup
logging.basicConfig(level=logging.DEBUG)

# init db
db.init_app(app)

# db setup
with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()

# blueprints
cuentas_claras = Blueprint("cuentas_claras_services", __name__, url_prefix="/cuentas-claras/")
api = Api(cuentas_claras)
app.register_blueprint(cuentas_claras)

# add resources
api.add_resource(ActividadesView, '/actividades')
api.add_resource(ViajeroView, '/viajeros')
api.add_resource(HealthCheckView, '/ping')

# Cors
cors = CORS(app=app, resources={r"/cuentas-claras/*": {"origins": "*"}})

# check-health-component at root level
@app.route('/ping', methods=['GET'])
def ping():
    app_name = os.getenv('FLASK_APP_NAME', 'cuentas_claras_services')
    return {"message":f"pong from {app_name} app"}
