from src.modelo.declarative_base import db

class Gasto(db.Model):

    __tablename__ = "gasto"

    id = db.Column(db.Integer, primary_key= True)
    fechaGasto = db.Column(db.Date)
    concepto = db.Column(db.String)
    valorGasto= db.Column(db.Float)
    viajero= db.relationship('Viajero', secondary='gasto_viajero')

class ActividadGasto(db.Model):

    __tablename__ = 'actividades_gasto'

    gasto_id = db.Column(db.String, db.ForeignKey('gasto.id'), primary_key=True)
    actividad_id = db.Column(db.String, db.ForeignKey('actividad.name'), primary_key=True)

# class GastoSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = Gasto
#         include_relationship = True
#         load_instance = True
#         exclude = ('viajero',)

