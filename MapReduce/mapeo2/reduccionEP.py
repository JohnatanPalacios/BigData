import sys


salida = {}

# Particionador 
for line in sys.stdin:
    line = line.strip()
    edad, valor = line.split('\t') # diag = diagnostico
    #print(edad, diag)
    
    if edad in salida:
        # si existe la llave agrega el valor
        salida[edad] += 1
    else:
        # si no existe la llave diagnostico
        salida[edad] = 0
        salida[edad] += 1

# Reducción = conteo o consolidación
print(salida)
print('Edades pacientes positivos en diabetes')
for edad in salida.keys():
    print('%s\t%s' % (edad, salida[edad]))
