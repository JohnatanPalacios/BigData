import db
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, Text


class Usuario(db.Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    descripcion = Column('descripcion', Text)
    activo = Column('activo', Boolean)
    edad = Column('edad', Integer)


class Comentario(db.Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True)
    mensaje = Column('mensaje', String(20))
    id_u = Column(Integer, ForeignKey('usuario.id'))
