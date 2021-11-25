# Reduccion
import sys
import db
from modelos import *
db.Base.metadata.create_all(db.motor)

# cat incautacion.csv | python3 MPDep.py | python3 RDDpto.py

# salida = {}
salida = []
# Particionador
for line in sys.stdin:
    line = line.strip()
    dpto, n = line.split('\t')

    if dpto not in salida:
        # salida[dpto] = 1
        salida.append(dpto)
        Add_Dpto(dpto)
        
print(salida)
