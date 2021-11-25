<h1>Big Data</h1> 
<h2>By: Johnatan Palacios</h2>

<p>En este repositorio encontrará herramientas de alta calidad para el trabajo de Big Data</p>

---
<h2>Se recomiendan las siguientes instalaciones</h2>

1. Python 3
```bash
python3 --version
sudo apt-get update
sudo apt-get install python3
```
2. Pip
```bash
sudo apt-get install python3-pip
```
3. Luigui
```bash
pip3 install luigi
```
4. MongoDB
```bash
sudo apt-get install -y mongodb-org
```
>si presenta algún fallo, omitir el "-org"
5. MariaDB
```bash
sudo apt update
sudo apt install mariadb-server
sudo mysql_secure_installation
```
>`mysql_secure_installation` le permitirá acceder a la configuración de mariadb.

---
<h2>¿Qué es ETL?</h2>

![](https://troyanx.com/Hefesto/tema03_procesoetl.png)

<p>ETL por sus siglas en inglés (Extract, Transform, Load).
Representa los procesos de:</p>

- <strong>Extracción:</strong> de datos crudos de diferentes fuentes.
- **Transformación:** según las necesidades de la empresa o la investigación a realizar.
  - Filtrar filas o columnas por ciertas características
  - Eliminar duplicidad
  - Limpiar datos
  - Dividir columnas
  - Entre muchos otras acciones.
- **Carga:** en la base de datos orientada a procesos analíticos (Target).

<p>Todo esto con la intención de encontrar los <strong>Insights</strong></p>

![](https://blog.bismart.com/hs-fs/hubfs/herramientas%20ETL%20tipos%20y%20para%20qu%C3%A9%20sirven.jpg?width=1366&name=herramientas%20ETL%20tipos%20y%20para%20qu%C3%A9%20sirven.jpg)

---
<h2>MapReduce</h2>
<p>info</p>

![](https://blogvisionarios.com/wp-content/uploads/2015/08/image_thumb_3_499DB43E.png)