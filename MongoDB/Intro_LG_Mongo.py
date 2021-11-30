# python3 Intro_LG_Mongo.py Extraer --local-scheduler
from pymongo import *
import luigi


IP='localhost'
PUERTO=27017
NOM_DB='Cultivos'
cliente=MongoClient(IP,PUERTO)
db=cliente[NOM_DB]


class Extraer(luigi.Task):
    def requires(self):
        return ()
    
    def run(self):
        consulta={'DEPARTAMENTO':'RISARALDA'}
        registro = db.Cacao.find_one(consulta)
        print(registro)


if __name__ == '__main__':
    ex = Extraer()
    ex.run()
