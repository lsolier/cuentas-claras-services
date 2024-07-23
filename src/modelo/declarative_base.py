from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker

#engine = create_engine('sqlite:///aplicacion.sqlite')
#Session = sessionmaker(bind=engine)

db = SQLAlchemy()

#Base = declarative_base()
#session = Session()