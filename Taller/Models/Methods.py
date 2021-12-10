from Models import db
from Models.ModelsSQL import *

def Guardar(model):
    db.session.add(model)
    db.session.commit()
    db.session.close()


def Add_Dpto(dpto, media):
    dp = Departamento(departamento=dpto,promedio=media)
    Guardar(dp)

def Add_Mpio(mpio):
    dp = Municipio(municipio=mpio)
    Guardar(dp)

def Add_Colegio(codane,cole,dpto,mpio,nat,ubi,gen):
    id_mp = (db.session.query(Municipio)
                .filter(Municipio.municipio==mpio)
                .first()
                .id)
    id_dp = (db.session.query(Departamento)
                .filter(Departamento.departamento==dpto)
                .first()
                .id)
    col = Colegio(codane=codane,
                    colegio=cole,
                    departamento=id_dp,
                    municipio=id_mp,
                    naturaleza=nat,
                    ubicacion=ubi,
                    genero=gen)
    Guardar(col)
    
                        
def Add_Est(pl,pm,pn,ps,pi,pg,col):
    cole = (db.session.query(Colegio)
                .filter(Colegio.colegio==col)
                .first()
                .codane)
    est = Estudiante(punt_lectura=pl,
                        punt_matematicas=pm,
                        punt_naturales=pn,
                        punt_sociales=ps,
                        punt_ingles=pi,
                        punt_global=pg,
                        colegio=cole)
    Guardar(est)
