import sys


salida = {}

# Particionador 
for line in sys.stdin:
    line = line.strip()
    edad, diag = line.split('\t') # diag = diagnostico
    #print(edad, diag)
    
    if diag in salida:
        # si existe la llave agrega el valor
        salida[diag].append(int(edad))
    else:
        # si no existe la llave diagnostico
        salida[diag] = []
        salida[diag].append(int(edad))

# Reducción = conteo o consolidación
#print(salida)
acum = 0

for diag in salida.keys():
    num_p = len(salida[diag])
    acum += num_p
    ls_edades = salida[diag]
    sum = 0
    for e in ls_edades:
        sum += e
    prom_e = sum/num_p
    print('%s\t%s' % (diag, prom_e))
print('Total de pacientes: ', acum)
