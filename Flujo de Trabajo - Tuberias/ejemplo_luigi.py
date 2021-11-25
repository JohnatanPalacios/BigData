import luigi
# python3 ejemplo_luigi.py Cuadrados --local-scheduler --n 35


class SalidaNumeros(luigi.Task):
    n = luigi.IntParameter()
    
    def requires(self):
        return []
    
    def output(self):
        return luigi.LocalTarget("numeros_{}.txt".format(self.n))
    
    def run(self):
        with self.output().open('w') as f:
            for i in range(1, self.n):
                f.write("{}\n".format(i))


class Cuadrados(luigi.Task):
    n = luigi.IntParameter(default=10)
    
    def requires(self):
        return [SalidaNumeros(n=self.n)]
    
    def output(self):
        return luigi.LocalTarget("cuadrados__{}.txt".format(self.n))
    
    def run(self):
        with self.input()[0].open() as fin, self.output().open('w') as fout:
            for line in fin:
                n = int(line.strip())
                val = n**2
                fout.write("{}:{}\n".format(n, val))


if __name__ == '__main__':
    luigi.run() # busca el que no tiene pre-requisitos para iniciar ahí
