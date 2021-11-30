<h1>Taller MongoDB</h1>

- Comandos básicos de mongo:
```bash
sudo service mongod start
sudo systemctl start mongod

sudo service mongod restart
sudo systemctl restart mongod

sudo service mongod stop
sudo systemctl stop mongod

sudo service mongod status
sudo systemctl status mongod
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


- <strong>Actualizar</strong>
```bash
db.libros.update({titulo:'la peste'}, {$set: {temas:['literatura','existencialismo']}})
```
```bash
db.COLLECTION.update({CONSULTA}, {$set:{INFO_UPDATE}})
```
  - Actualizar, agregando un nuevo valor:
  ```bash
  db.Empleados.update({Doc:8}, {$set: {Genero: 'F'}})
  ```

- Buscar todos los elementos que contengan un determinado string, se usará ```/string/``` para esto:
```bash
db.Empleados.find({Nombre:/Ana/}).pretty()
```

- <strong>Agregaciones</strong>:
  - Encontrar ```$match``` y agrupar sacando el promedio ```$group``` ```$avg```:
  ```bash
  db.Cacao.aggregate([
    {$match: {DEPARTAMENTO: 'RISARALDA'}},
    {$group: {_id: null, prom: {$avg: '$AreaSembrada'}}}
    ])
    ```
  - Encontrar ```$match``` y agrupar sacando el total ```$sum```:
  ```bash
  db.Cacao.aggregate([
    {$match: {DEPARTAMENTO: 'RISARALDA'}},
    {$group: {_id: null, total: {$sum: '$AreaSembrada'}}}
    ])
    ```
- Acciones fuera de la DB:
```bash
mongo --eval 'db.Cacao.findOne()' Cultivos
```
El retorno será:
```bash
{
	"_id" : ObjectId("61a179b0a40b89836615b6f5"),
	"DEPARTAMENTO" : "ANTIOQUIA",
	"Codmun" : 5120,
	"MUNICIPIO" : "CACERES",
	"CULTIVO" : "CACAO",
	"PERIODO" : 2018,
	"AreaSembrada" : 2044,
	"AreaCosechada" : 850,
	"Produccion" : 510,
	"Rendimiento" : 0.6
}
```

---
<h1><strong>MapReduce desde MongoDB</strong></h1>

- Departamentos:
```bash
var map = function(){
  emit(this.DEPARTAMENTO,1);
  }
var reduce = function(llave,valor){
  return Array.sum(valor);
}
db.Cacao.mapReduce(map,reduce, {out:'conteo'})
```

- AreaCosechada por Departamentos:
```bash
mongo < CacaoMRArea.js 
```
- AreaCosechada de Departamentos por Municipios:
```bash
mongo < CacaoMR_RisArea.js
```

---
<h1><strong>Exportar Datos</strong></h1>

```bash
mongoexport --db Cultivos --collection Area --type=csv --fields _id,value --out Areas_nacional.csv
```


---
<h1><strong>PyMongo</strong></h1>

- Instalar librería:
```bash
pip3 install pymongo
```

---
<h1><strong>Ingestión de Datos</strong></h1>
El archivo Cns_LgMongo.py plantea los inicios al tema de la ingestión de datos.

>MongoDB nos permite hacer pre procesamiento.
