import sys


salida = {}

# Agrupación
for linea in sys.stdin:
    #print(linea)
    linea = linea.strip()
    equipo, goles = linea.split('\t')
    if equipo == salida:
        salida[equipo].append(int(goles))
    else:
        salida[equipo] = []
        salida[equipo].append(int(goles))

# Reducción
for equipo in salida.keys():
    ls_goles = salida[equipo]
    sum_g = 0
    for g in ls_goles:
        sum_g += g
    pr_goles = sum_g / len(salida[equipo])
    print(equipo, 'promedio goles: ', pr_goles)
    