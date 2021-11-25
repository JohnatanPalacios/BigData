from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# dialecto://usuariodb:pwdb@ip:puerto/base_datos # para mysql
motor = create_engine('sqlite:///test.db')
Session = sessionmaker(bind=motor)
session = Session()
Base = declarative_base()

