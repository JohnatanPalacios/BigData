import luigi
from modelos import Add_Dpto
import db
# python3 LGDpto.py Departamento --local-scheduler


# Almacena departamento
class Departamento(luigi.Task):
    def requires(self):
        return []
    
    def output(self):
        return luigi.LocalTarget('dptos.txt')

    def run(self):
        origen = 'incautacion.csv'
        salida = []
        db.Base.metadata.create_all(db.motor)
        with open(origen) as fin, self.output().open('w') as fout:
            for line in fin:
                line = line.strip()
                cmp = line.split(',')
                if cmp[0] not in salida:
                    # si no existe la llave agrega el valor
                    salida.append(cmp[0])
                    Add_Dpto(cmp[0])
                    # fout.write('{}\n'.format(cmp[0]))


if __name__ == '__main__':
    luigi.run()
