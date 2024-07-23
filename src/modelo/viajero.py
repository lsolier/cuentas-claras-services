
from sqlalchemy import Column, Boolean, Integer, String, ForeignKey

from src.modelo.declarative_base import db

class Viajero(db.Model):
    __tablename__= 'viajero'

    id = db.Column(Integer, primary_key= True)
    nombre= db.Column(String(250))
    apellido= db.Column(String(250))
    identificadorViajero = db.Column(String(250))
    actividades = db.relationship('Actividad', secondary='actividades_viajero')
    gastos = db.relationship('Gasto', secondary='gasto_viajero')

class ActividadViajero(db.Model):
    __tablename__ = 'actividades_viajero'

    viajero_id = db.Column(
        String,
        ForeignKey('viajero.id'),
        primary_key=True)

    actividad_id = db.Column(
        String,
        ForeignKey('actividad.nombreActividad'),
        primary_key=True)

class GastoViajero(db.Model):
    __tablename__ = 'gasto_viajero'

    viajero_id = db.Column(
        String,
        ForeignKey('viajero.id'),
        primary_key=True)

    gasto_id = db.Column(
        String,
        ForeignKey('gasto.id'),
        primary_key=True)
