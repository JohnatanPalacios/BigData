# saber la cantidad de pacientes por edad que hay en cada caso

import sys

try:
    for line in sys.stdin:
        line = line.strip()
        line = line.split(",")
        # print(line)
        
        if len(line) == 10:
            edad = line[8]
            prueba = line[9]
            if prueba == 'tested_positive':
                print('%s\t 1' % (edad)) 
                # print(f"{edad} \t {prueba}")
except:
    pass
