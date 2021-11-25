# Mapeo
import sys


# cat incautacion.csv | python3 MPDep.py

try:
    for line in sys.stdin:
        line = line.strip()
        cmp = line.split(',')
        print('%s\t%s' % (cmp[0], 1)) # se debe enviar key value para mapreduce, si no hay value enviar 1
except:
    pass