from pymongo import *


if __name__ == '__main__':
    ip='localhost'
    puerto=27017
    cliente=MongoClient(ip,puerto)
    db=cliente['Cultivos']

    # registros = db['Cacao'].find_one()
    # registros = db.Cacao.find_one()
    consulta={'DEPARTAMENTO':'RISARALDA'}
    registros = db.Cacao.find_one(consulta)
    print(registros)