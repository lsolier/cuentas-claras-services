from src.modelo.declarative_base import db

class Viajero(db.Model):
    __tablename__ = 'viajero'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(250))
    lastname = db.Column(db.String(250))
    identificadorViajero = db.Column(db.String(250))
    actividades = db.relationship('Actividad', secondary='actividades_viajero', back_populates='viajeros')
    gastos = db.relationship('Gasto', secondary='gasto_viajero', back_populates='viajero')


class ActividadViajero(db.Model):
    __tablename__ = 'actividades_viajero'

    viajero_id = db.Column(db.Integer, db.ForeignKey('viajero.id'), primary_key=True)
    actividad_id = db.Column(db.String, db.ForeignKey('actividad.name'), primary_key=True)


class GastoViajero(db.Model):
    __tablename__ = 'gasto_viajero'

    viajero_id = db.Column(db.Integer, db.ForeignKey('viajero.id'), primary_key=True)
    gasto_id = db.Column(db.Integer, db.ForeignKey('gasto.id'), primary_key=True)

# class ActividadViajeroSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = ActividadViajero
#         include_relationship = True
#         load_instance = True
#
# class GastoViajeroSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = GastoViajero
#         include_relationship = True
#         load_instance = True
