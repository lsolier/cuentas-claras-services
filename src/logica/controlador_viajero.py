from src.modelo.declarative_base import db
from src.modelo.viajero import Viajero

class ControladorViajero:

    def __init__(self):
        super().__init__()
        #Base.metadata.create_all(engine)

    def agregar_viajero(self, nombre, apellido):
        identificadorViajero = nombre+apellido
        viajero = db.session.query(Viajero).filter(Viajero.identificadorViajero == identificadorViajero).first()
        if viajero is None:
            viajero = Viajero(nombre=nombre,
                              apellido=apellido,
                              identificadorViajero=identificadorViajero)
            db.session.add(viajero)
            db.session.commit()
            return True
        else:
            return False

    def agregar_viajero_obj(self, viajeroObj):
        db.session.add(viajeroObj)
        db.session.commit()
        return True

    def editar_viajero(self, nombre, apellido, nuevoNombre, nuevoApellido):
        identificadorViajero = nombre + apellido
        nuevoIdentificadorViajero = nuevoNombre + nuevoApellido
        viajero = db.session.query(Viajero).filter(Viajero.identificadorViajero == identificadorViajero).first()
        if viajero is not None:
            viajero.nombre = nuevoNombre
            viajero.apellido = nuevoApellido
            viajero.identificadorViajero = nuevoIdentificadorViajero
            db.session.commit()
            return True
        else:
            return False

    def eliminar_viajero(self, nombre, apellido):
        identificadorViajero = nombre + apellido
        viajero = db.session.query(Viajero).filter(Viajero.identificadorViajero == identificadorViajero).first()
        if viajero is not None:
            db.session.delete(viajero)
            db.session.commit()
            return True
        else:
            return False

    def get_viajeros(self):
        viajeros = db.session.query(Viajero).all()
        if viajeros != None:
            return viajeros
        else:
            return []

    def get_viajero(self, nombre, apellido):
        identificadorViajero = nombre + apellido
        return db.session.query(Viajero).filter(Viajero.identificadorViajero == identificadorViajero).first()
    def get_viajero_id(self, identificadorViajero):
        return db.session.query(Viajero).filter(Viajero.identificadorViajero == identificadorViajero).first()
