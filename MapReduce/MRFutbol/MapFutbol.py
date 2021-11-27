import sys

try:
    con=0
    for linea in sys.stdin:
        if con>0:
            linea=linea.strip()
            ls=linea.split(',')
            #print(ls[3].rstrip(), ls[5])
            #Equipo local, goles local
            print ( '%s\t%s' % (ls[3].rstrip(),ls[5]))
        con+=1
except:
    pass
#print ('Cantidad de registros: ', con)
