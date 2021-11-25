import sys
# python3 sondeo.py incautacion.csv 10

if __name__ == '__main__':
    arg = sys.argv
    if len(arg) == 3:
        nom_ar = arg[1]
        limite = int(arg[2])
        print('Nombre archivo: ', arg[1])
        print('Limite de datos: ', limite)
        archivo = open(nom_ar, 'r')

        con = 0
        ignorar_head = False
        for linea in archivo:
            linea = linea.strip()
            campos = linea.split(',')
            if ignorar_head: ignorar_head = False
            else:
                print(campos[0], campos[1], campos[2], campos[3], campos[4],campos[5])
            if con > limite: break
            con += 1
    else:
        print('###----- Argumentos incorrectos -----###')
