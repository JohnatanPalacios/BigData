from Models import db
from sqlalchemy import Column, Integer, ForeignKey, Text, Float, String
from sqlalchemy.orm import relationship


class Departamento(db.Base):
    __tablename__ = 'departamento'
    id = Column(Integer, primary_key=True)
    departamento = Column('departamento', Text)
    promedio = Column('promedio', Float)
    colegio = relationship('Colegio')


class Municipio(db.Base):
    __tablename__ = 'municipio'
    id = Column(Integer, primary_key=True)
    municipio = Column('municipio', Text)
    colegio = relationship('Colegio')


class Colegio(db.Base):
    __tablename__ = 'colegio'
    codane = Column('codane', String(20), primary_key=True)
    colegio = Column('colegio', Text)
    departamento = Column(Integer, ForeignKey('departamento.id'))
    municipio = Column(Integer, ForeignKey('municipio.id'))
    naturaleza = Column('naturaleza', Text)
    ubicacion = Column('ubicacion', Text)
    genero = Column('genero', Text)
    estudiante = relationship('Estudiante')


class Estudiante(db.Base):
    __tablename__ = 'estudiante'
    nombre = Column('nombre', Integer, primary_key=True)
    punt_lectura = Column('punt_lectura', Float)
    punt_matematicas = Column('punt_matematicas', Float)
    punt_naturales = Column('punt_naturales', Float)
    punt_sociales = Column('punt_sociales', Float)
    punt_ingles = Column('punt_ingles', Float)
    punt_global = Column('punt_global', Float)
    colegio = Column(String(20), ForeignKey('colegio.codane'))
