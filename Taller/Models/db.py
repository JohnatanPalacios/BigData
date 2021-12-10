from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

motor = create_engine('mysql+pymysql://admin:careloko@localhost:3306/taller2')
Session = sessionmaker(bind=motor)
session = Session()
Base = declarative_base()