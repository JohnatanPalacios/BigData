# python3 Cns_LgMongo.py Extraer --local-scheduler
import os
import luigi
from pymongo import *


IP='localhost'
PUERTO=27017
NOM_DB='Cultivos'
cliente=MongoClient(IP,PUERTO)
db=cliente[NOM_DB]


class SalidaConsulta(luigi.Task):
    def requires(self):
        return []

    def output(self):
        return luigi.LocalTarget('InfoAntioquia.csv')
    
    def run(self):
        os.system('mongo < cacaoAntioquia.js')
        os.system('mongoexport --db Cultivos --collection=Antioquia --type=csv --fields _id,value --out InfoAntioquia.csv')


class Extraer(luigi.Task):
    def requires(self):
        return [SalidaConsulta()]
    
    def output(self):
        return []
    
    def run(self):
        with self.input()[0].open() as fin:
            for linea in fin:
                linea = linea.strip()
                cad = linea.split(',')
                reg = {cad[0]:cad[1]}
                print(reg)


if __name__ == '__main__':
    luigi.run()