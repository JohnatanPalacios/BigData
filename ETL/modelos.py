import db
from sqlalchemy import Column, Integer, ForeignKey, Text, Float, String
from sqlalchemy.orm import relationship


def Guardar(model):
    db.session.add(model)
    db.session.commit()
    db.session.close()

def Add_Dpto(dp):
    dpto = Departamento(dpto=dp)
    Guardar(dpto)

def Add_Mpio(cd,mp,id_dp):
    muni = Municipio(codane=cd, mpio=mp, id_dpto=id_dp)
    Guardar(muni)

def Add_Registro(cb, fh, cant, cd):
    inca = Incautacion(clasebien=cb,
                        fecha=fh,
                        cant=cant,
                        cd_mpio=cd)
    Guardar(inca)


class Departamento(db.Base):
    __tablename__ = 'departamento'
    id = Column(Integer, primary_key=True)
    dpto = Column('departamento', Text)
    municipio = relationship('Municipio')


class Municipio(db.Base):
    __tablename__ = 'municipio'
    codane = Column('codigo_dane', String(20), primary_key=True)
    mpio = Column('municipio', Text)
    id_dpto = Column(Integer, ForeignKey('departamento.id'))
    incautacion = relationship('Incautacion')


class Incautacion(db.Base):
    __tablename__ = 'incautacion'
    id = Column(Integer, primary_key=True)
    clasebien = Column('clase_bien', Text)
    fecha = Column('fecha_hecho', Text)
    cant = Column('cantidad', Text)
    cd_mpio = Column(String(20), ForeignKey('municipio.codane'))
