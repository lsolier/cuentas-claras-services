import json

import requests

from flask_restful import Resource
from flask import request
from src.logica.adaptador_actividad import AdaptadorActividad
from src.modelo.schemas import ActividadSchema, ViajeroSchema

actividad_schema = ActividadSchema()
viajero_schema = ViajeroSchema()
adaptadorActividad = AdaptadorActividad()

class HealthCheckView(Resource):
    def get(self):
        return {"message": "pong", "status": "success"}

class ActividadesView(Resource):

    def get(self):
        actividades = adaptadorActividad.listar_actividades().result
        return actividad_schema.dump(actividades, many=True), requests.codes.ok

    def post(self):
        nombre = request.json['nombre']
        try:
            adaptadorActividad.agregar_actividad(nombre)
        except Exception as err:
            print("Error al insertar usando adaptadorActividad")
            return err.messages_dict, requests.codes.bad_request

        return {"mensaje": "Actividad Creada"}, requests.codes.created

class ViajeroView(Resource):

    def get(self):
        viajeros = adaptadorActividad.get_viajeros().result
        return viajero_schema.dump(viajeros, many=True), requests.codes.ok

    def post(self):
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        try:
            adaptadorActividad.add_viajero(nombre, apellido)
        except Exception as err:
            print("Error al insertar usando adaptadorActividad")
            return err.messages_dict, requests.codes.bad_request

        return {"mensaje": "Viajero Creado"}, requests.codes.created