from pymongo import *

client = MongoClient('mongodb://localhost:27017/')
db = client['Saber11']

results = db.s20201.find({"COLE_CALENDARIO":"B"})

for r in results:
    print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (r["COLE_COD_DANE_SEDE"],
                                                                    r["COLE_NOMBRE_SEDE"],
                                                                    r["COLE_DEPTO_UBICACION"],
                                                                    r["COLE_MCPIO_UBICACION"],
                                                                    r["COLE_NATURALEZA"],
                                                                    r["COLE_AREA_UBICACION"],
                                                                    r["COLE_GENERO"],
                                                                    r["PUNT_LECTURA_CRITICA"],
                                                                    r["PUNT_MATEMATICAS"],
                                                                    r["PUNT_C_NATURALES"],
                                                                    r["PUNT_SOCIALES_CIUDADANAS"],
                                                                    r["PUNT_INGLES"],
                                                                    r["PUNT_GLOBAL"]))
