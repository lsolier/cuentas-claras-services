from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.modelo.actividad import Actividad
from src.modelo.viajero import Viajero


class ActividadSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Actividad
        include_relationships = True
        load_instance = True

class ViajeroSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Viajero
        include_relationships = True
        load_instance = True
