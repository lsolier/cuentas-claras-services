from src.modelo.declarative_base import db

class Actividad(db.Model):
    __tablename__ = "actividad"

    nombreActividad = db.Column(db.String(250), primary_key=True)
    estadoActividad = db.Column(db.Boolean)
    viajeros = db.relationship('Viajero', secondary='actividades_viajero', back_populates='actividades')
    gastos = db.relationship('Gasto', secondary='actividades_gasto')