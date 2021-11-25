# Ingestion de datos para Departamentos
# Requerimientos: archivo-csv cantidad_datos
# Llamada bash: python3 ingDpto.py incautacion.csv 10
import sys
import db
from modelos import *


def Add_Dpto(dp):
    dpto = Departamento(dpto=dp)
    db.session.add(dpto)
    db.session.commit()


if __name__ == '__main__':
    arg = sys.argv
    if len(arg) == 3:
        nom_ar = arg[1]
        limite = int(arg[2])
        print('Nombre archivo: ', arg[1])
        print('Limite de datos: ', limite)
        archivo = open(nom_ar, 'r')

        db.Base.metadata.create_all(db.motor)

        con = 0
        ignorar_head = True
        for linea in archivo:
            linea = linea.strip()
            campos = linea.split(',')
            if ignorar_head: ignorar_head = False
            else:
                # buscar el dpto a ingresar, si no existe se debe agregar
                dp = db.session.query(Departamento).filter(Departamento.dpto).all()
                Add_Dpto(campos[0])
            if con > limite: break
            con += 1
    else:
        print('###----- Argumentos incorrectos -----###')


# ls_datos = {} # proxima clase