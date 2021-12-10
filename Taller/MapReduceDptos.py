from pymongo import *
from bson.code import Code
from Models import db as sql
from Models.Methods import Add_Dpto


sql.Base.metadata.create_all(sql.motor)

client = MongoClient('mongodb://localhost:27017/')
db = client['Saber11']
s20201 = db['s20201']

map = Code ("function(){if(this.COLE_CALENDARIO=='B'){emit(this.COLE_DEPTO_UBICACION,this.PUNT_GLOBAL)}}")
reduce = Code ("function(llave,valor){return Array.avg(valor)}")

result = s20201.map_reduce(map, reduce, "myresults")
dptos = []

for r in result.find():
    dpto = r['_id']
    promedio = round(float(r['value']), 2)
    if dpto not in dptos:
        dptos.append(dpto)
        Add_Dpto(dpto, promedio)
