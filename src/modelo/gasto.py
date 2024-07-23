

from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship

#from .declarative_base import Base
from src.modelo.declarative_base import db

class Gasto(db.Model):

    __tablename__ = "gasto"

    id = db.Column(Integer, primary_key= True)
    fechaGasto = db.Column(Date)
    concepto = db.Column(String)
    valorGasto= db.Column(Float)
    viajero= db.relationship('Viajero', secondary='gasto_viajero')

class ActividadGasto(db.Model):

    __tablename__ = "actividades_gasto"

    gasto_id = db.Column(
        String,
        ForeignKey('gasto.id'),
        primary_key=True)
    actividad_id = db.Column(
        String,
        ForeignKey('actividad.nombreActividad'),
        primary_key=True)