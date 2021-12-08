import db
from Taller.Models.Models import *

def Guardar(model):
    db.session.add(model)
    db.session.commit()
    db.session.close()


def Add_Model(**kwargs):
    if 'departamento' in kwargs:
        Guardar(Departamento(codigo= kwargs['codigo'],
                            departamento=kwargs['departamento'],
                            promedio=kwargs['promedio']))
    elif 'municipio' in kwargs:
        Guardar(Municipio(codigo= kwargs['codigo'],
                            municipio=kwargs['municipio']))
    elif 'naturaleza' in kwargs:
        Guardar(Naturaleza(naturaleza=kwargs['naturaleza']))
    elif 'ubicacion' in kwargs:
        Guardar(Ubicacion(ubicacion=kwargs['ubicacion']))
    elif 'colegio' in kwargs:
        Guardar(Colegio(codane=kwargs['codane'],
                        colegio=kwargs['colegio'],
                        punt_area_total=kwargs['punt_area_total'],
                        punt_global_total=kwargs['punt_global_total'],
                        municipio=kwargs['municipio'],
                        departamento=kwargs['departamento'],
                        naturaleza=kwargs['naturaleza'],
                        ubicacion=kwargs['ubicacion'],
                        genero=kwargs['genero']))
    elif 'estudiante' in kwargs:
        Guardar(Estudiante(nombre=kwargs['nombre'],
                            punt_lectura_critica=kwargs['punt_lectura_critica'],
                            punt_matematicas=kwargs['punt_matematicas'],
                            punt_ciencias_naturales=kwargs['punt_ciencias_naturales'],
                            punt_sociales_ciudadanas=kwargs['punt_sociales_ciudadanas'],
                            punt_ingles=kwargs['punt_ingles'],
                            punt_global=kwargs['punt_global'],
                            colegio=kwargs['colegio']))
