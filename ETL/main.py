# cat incautacion.csv | python3 main.py
import sys
import db
from modelos import *
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
db.Base.metadata.create_all(db.motor)


dptos = []
mpios = []
ignore_head = True

for line in sys.stdin:
    if ignore_head: ignore_head = False
    else:
        linea = line.strip()
        campos = linea.split(',')

        dpto = campos[0]
        mpio = campos[1]
        codane = campos[2]
        clasebien = campos[3]
        fecha = campos[4]
        cant = campos[5] # float(campos[5])

        if dpto not in dptos:
            dptos.append(dpto)
            Add_Dpto(dpto)
            logger.info("Creando departamento {} en la BD".format(dpto))
        if mpio not in mpios:
            mpios.append(mpio)
            id_dp = (db.session.query(Departamento)
                    .filter(Departamento.dpto==dpto)
                    .first()
                    .id)
            Add_Mpio(codane, mpio, id_dp)
            logger.info("Creando municipio {} en la BD".format(mpio))
        
        id_mp = (db.session.query(Municipio)
                    .filter(Municipio.mpio==mpio)
                    .first()
                    .codigodane)
        
        if id_mp: Add_Registro(clasebien, fecha, cant, id_mp)
        else: print('%s\t%s\t%s\t%s\t' % (clasebien, fecha, cant, codane))
        logger.info("Registrando incautación {} {} {} {} en la BD".format(clasebien, fecha, cant, codane))
