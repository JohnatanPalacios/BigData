# Reduccion
import sys
import db
from modelos import *
db.Base.metadata.create_all(db.motor)

# cat incautacion.csv | python3 MPMpio.py | python3 RDMpio.py

salida = []
ignorar_head = True
# Particionador
for line in sys.stdin:
    line = line.strip()
    dpto, mpio, codane = line.split('\t')

    if ignorar_head: ignorar_head = False
    else:
        if mpio not in salida:
            salida.append(mpio)
            dpto = (db.session.query(Departamento).filter(Departamento.dpto==dpto).first()).id
            Add_Mpio(codane, mpio, dpto)
            # print('%s\t%s\t%s' % (codane, mpio, dpto))

print(salida)
