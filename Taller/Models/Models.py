import db
from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship


class Departamento(db.Base):
    __tablename__ = 'departamento'
    codigo = Column(Integer, primary_key=True)
    departamento = Column('departamento', Text)
    promedio = Column('promedio', Integer)
    colegio = relationship('Colegio')


class Municipio(db.Base):
    __tablename__ = 'municipio'
    codigo = Column(Integer, primary_key=True)
    municipio = Column('municipio', Text)
    colegio = relationship('Colegio')


class Genero(db.Base):
    __tablename__ = 'genero'
    id = Column(Integer, primary_key=True)
    genero = Column('genero', Text)
    colegio = relationship('Colegio')


class Colegio(db.Base):
    __tablename__ = 'colegio'
    codane = Column(Integer, primary_key=True)
    colegio = Column('colegio', Text)
    punt_total_lectura = Column('punt_total_lectura', Integer)
    punt_total_matematicas = Column('punt_total_matematicas', Integer)
    punt_total_naturales = Column('punt_total_naturales', Integer)
    punt_total_sociales = Column('punt_total_sociales', Integer)
    punt_total_ingles = Column('punt_total_ingles', Integer)
    punt_global_total = Column('punt_global_total', Integer)
    naturaleza = Column('naturaleza', Text)
    ubicacion = Column('ubicacion', Text)
    municipio = Column(Integer, ForeignKey('municipio.codigo'))
    departamento = Column(Integer, ForeignKey('departamento.codigo'))
    genero = Column(Integer, ForeignKey('genero.id'))
    estudiante = relationship('estudiante')


class Estudiante(db.Base):
    __tablename__ = 'estudiante'
    nombre = Column(Integer, primary_key=True)
    punt_lectura_critica = Column('punt_lectura_critica', Integer)
    punt_matematicas = Column('punt_matematicas', Integer)
    punt_ciencias_naturales = Column('punt_ciencias_naturales', Integer)
    punt_sociales_ciudadanas = Column('punt_sociales_ciudadanas', Integer)
    punt_ingles = Column('punt_ingles', Integer)
    punt_global = Column('punt_global', Integer)
    colegio = Column(Integer, ForeignKey('colegio.codane'))
