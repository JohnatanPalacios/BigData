<h1><strong>Big Data</strong></h1>
<h3>12-11-2021</h3>

<h2>Pasos</h2>

1. Instalación DB MariaDB:
```bash
  sudo apt install mysql-server
  password: Careloko77
  sudo mysql
```

2. usuario y contraseña de la DB
```mysql
  CREATE USER 'admin'@'localhost' IDENTIFIED BY 'BigData*7';
```
  - >La clave puede ser **careloko**

3. Instalación MySQL
4. Probar acceso
```mysql
  mysql -u admin -p
```
  > La contraseña es **careloko**

  >En caso de error al escribir contraseña usar **ctrl+u**

- mostrar bases de datos:
```mysql
show databases;
```

- crear bases de datos:
```mysql
CREATE SCHEMA name;
```

En caso de no permitir creación de la DB
Para dar permisos se debe salir de la DB y entrar como super usuario desde el shell:
```bash
sudo mysql
```

- Dar permisos:
```mysql
GRANT ALL PRIVILEGES ON * . * TO 'admin'@'localhost';
```

- Reiniciar privilegios para que tengan efecto:
```mysql
FLUSH PRIVILEGES;
```

5. Crear programa de gestión de DB usando Python
