# Mapeo
import sys


# cat incautacion.csv | python3 MPMpio.py

try:
    for line in sys.stdin:
        line = line.strip()
        cmp = line.split(',')
        print('%s\t%s\t%s' % (cmp[0], cmp[1], cmp[2])) # se debe enviar key value para mapreduce, si no hay value enviar 1
except:
    pass
