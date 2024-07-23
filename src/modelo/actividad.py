
from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
#from .declarative_base import Base
from src.modelo.declarative_base import db


class Actividad(db.Model):

    __tablename__ = "actividad"

    nombreActividad = db.Column(String(250), primary_key= True)
    estadoActividad = db.Column(Boolean)
    viajeros = db.relationship('Viajero', secondary='actividades_viajero')
    gastos = db.relationship('Gasto', secondary='actividades_gasto')
