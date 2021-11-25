import sys
import csv
import db
from modelos import *

# Requerimientos: archivo-csv cantidad_datos
# python3 sondeo.py incautacion.csv 10
# [sondeo.py incautacion.csv 10]


def Add_Dpto(dp):
    dpto = Departamento(dpto=dp)
    db.session.add(dpto)
    db.session.commit()

def Add_Municipio(cd,mp,id_dp):
    muni = Municipio(codigodane=cd, municipio=mp, id_dpto=id_dp)
    db.session.add(muni)
    db.session.commit()

def Add_Registro(cd, cb, fh, cant):
    inca = Incautacion(codigodane=cd,
                        clasebien=cb,
                        fecha=fh,
                        cantidad=cant)
    db.session.add(inca)
    db.session.commit()


if __name__ == '__main__':
    arg = sys.argv
    if len(arg) == 3:
        nom_ar = arg[1]
        limite = int(arg[2])
        print('Nombre archivo: ', arg[1])
        print('Limite de datos: ', limite)
        archivo = open(nom_ar, 'r')

        # db.Base.metadata.create_all(db.motor)

        con = 0
        ignorar_head = True
        for linea in archivo:
            linea = linea.strip()
            campos = linea.split(',')
            if ignorar_head: ignorar_head = False
            else:
                # Add_Registro(campos[0],
                #             campos[1],
                #             campos[2],
                #             campos[3],
                #             campos[4],
                #             float(campos[5]))
                # print(campos)
                print(campos[0], campos[1], campos[2], campos[3], campos[4],campos[5])
            if con > limite: break
            con += 1
    else:
        print('###----- Argumentos incorrectos -----###')


# ls_datos = {} # proxima clase