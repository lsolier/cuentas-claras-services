
from src.modelo.gasto import Gasto
from src.modelo.declarative_base import db

class ControladorGasto:

    def __init__(self):
        super().__init__()
        #Base.metadata.create_all(engine)

    def add_gasto_obj(self,gasto):
        try:
            db.session.add(gasto)
            db.session.commit()
            return True
        except:
            return False

    def get_gasto(self, gastoId):
            gasto = db.session.query(Gasto).filter(Gasto.id == gastoId).first()
            return gasto

    def edit_gasto(self,gasto):
        try:
            dbGasto= db.session.query(Gasto).filter(Gasto.id == gasto.id).first()
            if dbGasto != None:
                dbGasto.fechaGasto = gasto.fechaGasto
                dbGasto.valorGasto = gasto.valorGasto
                dbGasto.viajero = gasto.viajero
                dbGasto.concepto = gasto.concepto
                db.session.commit()
                return True
            else:
                self.add_gasto_obj(gasto)
        except:
            return False
    def delete_gasto(self,gastoId):
        try:
            dbGasto = db.session.query(Gasto).filter(Gasto.id == gastoId).first()
            db.session.delete(dbGasto)
            db.session.commit()
            return True
        except:
            return False
    def delete_all_gastos(self):
        try:
            gastos= db.session.query(Gasto).all()
            if gastos != None :
                for gasto in gastos:
                    db.session.delete(gasto)
                db.session.commit()
            return True
        except:
            return False