<h1>Taller MongoDB</h1>

- Comandos básicos de mongo:
```bash
sudo service mongod restart
sudo service mongod start
sudo service mongod stop
sudo service mongod status
```

<h2>Importar un archivo a MongoDB</h2>

```bash
mongoimport --db Cultivos --collection Cacao --type=csv --file prod_cacao_dpt.csv --headerline
```

<h2>Comandos MongoDB</h2>

- Ver bases de datos:
```bash
show dbs
```
- Entrar (seleccioanr) la base de datos a trabajar:
```bash
use Cultivos
```
- Ver coleciones:
```bash
show collections
```
- Seleccionar colección y buscar primera ocurrencia:
```bash
db.Cacao.findOne()
```
- Buscar un departamento, traer primera ocurrencia:
```bash
db.Cacao.findOne({'DEPARTAMENTO':'RISARALDA'})
```
- Listar los departamentos:
```bash
db.Cacao.distinct('DEPARTAMENTO')
```
- Listar municipios de un departamento:
```bash
db.Cacao.distinct('MUNICIPIO', {DEPARTAMENTO:'RISARALDA'})
```
- Contar elementos:
```bash
db.Cacao.count()
db.Cacao.find({DEPARTAMENTO:'ANTIOQUIA'}).count()
```
- Limitar listado:
```bash
db.Cacao.find({DEPARTAMENTO:'ANTIOQUIA'}).limit(5)
```
- Listar con límite y mostrar con formato:
```bash
db.Cacao.find({DEPARTAMENTO:'ANTIOQUIA'}).count().pretty()
```
- <strong>Búsquedas numéricas:</strong>
  - Menor a 600:
```bash
db.Cacao.find({AreaSembrada: {$lt:600}}).count()
```
  - Menor igual a 600:
```bash
db.Cacao.find({AreaSembrada: {$lte:600}}).count()
```
  - Igual a 600:
```bash
db.Cacao.find({AreaSembrada: {$gt:600}}).count()
```
  - Mayor igual a 600:
```bash
db.Cacao.find({AreaSembrada: {$gte:600}}).count()
```
  - Diferente a 600:
```bash
db.Cacao.find({AreaSembrada: {$ne:600}}).count()
```
  - Búsqueda numérica anidada a 600:
```bash
db.Cacao.find({AreaSembrada: {$gte:600}, DEPARTAMENTO:'RISARALDA', PERIODO:2018}).pretty()
```
- <strong>Búsquedas con ordenamiento:</strong>
  - Ascendente para municipio:
```bash
db.Cacao.find({DEPARTAMENTO:'RISARALDA', PERIODO:2018}).sort({MUNICIPIO:1}).pretty()
```
  - Descendente para municipio:
```bash
db.Cacao.find({DEPARTAMENTO:'RISARALDA', PERIODO:2018}).sort({MUNICIPIO:-1}).pretty()
```
- Búsqueda con un filtro y luego las columnas que quiere ```...find({filtro}, {columnas})```:
```bash
db.Cacao.find({DEPARTAMENTO:'RISARALDA', PERIODO:2018}, {MUNICIPIO:1, PERIODO:1, AreaSembrada:1}).limit(2)
```
- <strong>Consultas And-Or:</strong>
- Or:
```bash
db.Cacao.find({$or:[{DEPARTAMENTO:'VICHADA'}, {DEPARTAMENTO:'AMAZONAS'}]})
```
- And:
```bash
db.Cacao.find({$and:[{AreaCosechada:{$gt:5}}, {DEPARTAMENTO:'AMAZONAS'}]})
```
- <strong>Agregaciones</strong>: