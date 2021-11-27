import sys

salida={}
#Agrupacion
for linea in sys.stdin:

    linea =linea.strip()
    eqp, goles= linea.split('\t')
    if eqp in salida:
        salida[eqp].append(int(goles))
    else:
        salida[eqp]=[]
        salida[eqp].append(int(goles))

#Reduccion
for eqp in salida.keys():
    ls_goles=salida[eqp]
    sum_g=0
    for g in ls_goles:
        sum_g+=g
    pr_goles=sum_g/len(salida[eqp])
    print (eqp, ' promedio goles: ', pr_goles)
