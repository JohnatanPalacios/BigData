from pymongo import *


if __name__ == '__main__':
    ip='localhost'
    puerto=27017
    cliente=MongoClient(ip,puerto)
    db=cliente['Cultivos']

    consulta={'DEPARTAMENTO':'RISARALDA', 'PERIODO':2018}
    registros = db.Cacao.find(consulta)
    
    for r in registros:
        print(r['MUNICIPIO'], r['PERIODO'], type(r))
