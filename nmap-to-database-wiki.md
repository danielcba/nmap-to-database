# Escaneo de Red con Nmap y Almacenamiento en MariaDB

Este proyecto realiza un escaneo de red utilizando la biblioteca `nmap` y almacena los resultados en una base de datos MariaDB. A continuación, se detalla el funcionamiento del código y cómo configurarlo.

## Requisitos

- Python 3.x
- Biblioteca `nmap`
- Biblioteca `mysql-connector-python`
- Servidor MariaDB/MySQL

## Instalación

1. Crear y activar un entorno virtual (opcional pero recomendado):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Instalar las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

3. Información de la biblioteca nmap:
   ```bash
   https://www.pythonparatodo.com/?p=251
   ```

## Configuración de la Base de Datos

1. Conéctate a tu servidor MariaDB/MySQL y crea la base de datos y la tabla necesarias ejecutando las siguientes líneas SQL:

   ```sql
   CREATE SCHEMA `basenmap`;

   CREATE TABLE `basenmap`.`nmap` (
     `host` VARCHAR(15) NULL,
     `hostname` VARCHAR(64) NULL,
     `hostname_type` VARCHAR(16) NULL,
     `protocol` VARCHAR(8) NULL,
     `port` VARCHAR(5) NULL,
     `name` VARCHAR(20) NULL,
     `state` VARCHAR(16) NULL,
     `product` VARCHAR(32) NULL,
     `extrainfo` VARCHAR(64) NULL,
     `reason` VARCHAR(16) NULL,
     `version` VARCHAR(32) NULL,
     `conf` VARCHAR(3) NULL,
     `cpe` VARCHAR(64) NULL
   );
   ```

## Programación de la Ejecución del Script

Si deseas que el script se ejecute automáticamente cada cierto tiempo, puedes configurarlo como una tarea programada (cron job) en tu sistema operativo. A continuación, se explica cómo hacerlo.

### Configuración de Crontab

1. Abre el editor de crontab para el usuario actual:

   ```bash
   crontab -e
   ```

2. Añade la siguiente línea al final del archivo para ejecutar el script cada 2 minutos:

   ```bash
   */2 * * * * /usr/bin/python3 /home/username/base-nmap/nmap-to-base.py
   ```

   Esta línea programa la ejecución del script `nmap-to-base.py` cada 2 minutos. Si deseas cambiar la frecuencia, ajusta el primer campo (\*/2) según tus necesidades. Aquí hay algunos ejemplos:

   - Cada 5 minutos:
     ```bash
     */5 * * * * /usr/bin/python3 /home/username/base-nmap/nmap-to-base.py
     ```
   - Cada hora:
     ```bash
     0 * * * * /usr/bin/python3 /home/username/base-nmap/nmap-to-base.py
     ```
   - Todos los días a las 3 AM:
     ```bash
     0 3 * * * /usr/bin/python3 /home/username/base-nmap/nmap-to-base.py
     ```

### Guardar y Salir

- En el editor de crontab, guarda los cambios y cierra el editor. En `nano`, por ejemplo, presiona `CTRL+O` para guardar y `CTRL+X` para salir.

### Verificación

- Para verificar que la tarea se ha añadido correctamente, puedes listar las tareas programadas:
  ```bash
  crontab -l
  ```

### Nota de Seguridad

Asegúrate de que el script `nmap-to-base.py` tenga permisos de ejecución y que el usuario que configura el cron job tenga los permisos necesarios para ejecutar el script y acceder a la base de datos.

## Descripción del Código

### Importación de Bibliotecas

```python
import nmap
import time
import mysql.connector
from mysql.connector.constants import ClientFlag
```

- `nmap`: Biblioteca para realizar escaneos de red.
- `time`: Biblioteca para medir el tiempo del escaneo.
- `mysql.connector`: Biblioteca para interactuar con la base de datos MariaDB/MySQL.

### Configuración Inicial

```python
starting_point = time.time()
ns = nmap.PortScanner()
```

- `starting_point`: Marca el tiempo de inicio del escaneo.
- `ns`: Crea un objeto `PortScanner` de `nmap`.

### Parámetros del Escaneo

```python
ns.scan("192.168.0.1-255 -sC --version-intensity 9 -sS -sV --open -PE -T5")
```

- `192.168.0.1-255`: Rango de IPs a escanear.
- `-sC`: Ejecución de scripts básicos de Nmap.
- `--version-intensity 9`: Intensidad máxima para la detección de versiones.
- `-sS`: Escaneo SYN (semi-abierto).
- `-sV`: Detección de versiones de servicios.
- `--open`: Solo reportar puertos abiertos.
- `-PE`: Utilizar pings para mejorar la visibilidad de la red.
- `-T5`: Ajuste de la velocidad del escaneo (muy agresivo).

### Guardar Resultados del Escaneo

```python
f = open("/home/username/base-nmap/scan.csv", "w")
f.write(ns.csv())
f.close()
```

- Abre un archivo para escribir los resultados en formato CSV.
- Escribe los resultados del escaneo en el archivo.
- Cierra el archivo.

### Conexión a la Base de Datos y Carga de Datos

```python
conexion1 = mysql.connector.connect(
    host="localhost",
    user="username",
    passwd="password",
    database="basenmap",
    allow_local_infile=True,
)

cursor1 = conexion1.cursor()
cursor1.execute(
    "load data local infile '/home/username/base-nmap/scan.csv' into table nmap FIELDS TERMINATED BY ';' LINES TERMINATED BY '\n' IGNORE 1 LINES"
)
conexion1.commit()
conexion1.close()
cursor1.close()
```

- Conecta a la base de datos `basenmap`.
- Crea un cursor para ejecutar comandos SQL.
- Carga los datos del archivo CSV en la tabla `nmap`.
- Confirma los cambios y cierra la conexión y el cursor.

### Tiempo Transcurrido

```python
elapsed_time = time.time() - starting_point
elapsed_time_int = int(elapsed_time)
print(f"Scanning completed in {elapsed_time:.2f} seconds")
```

- Calcula el tiempo transcurrido desde el inicio del escaneo.
- Convierte el tiempo transcurrido a segundos.
- Imprime el tiempo total del escaneo en segundos con dos decimales.

## Advertencias de Seguridad

- **No almacenar credenciales directamente en el código.** Utilizar variables de entorno o un archivo de configuración seguro.
- **Permitir `allow_local_infile` con precaución.** Puede representar un riesgo de seguridad si se permite desde fuentes no confiables.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

---

Este archivo README.md proporciona una explicación detallada del código, cómo configurarlo e instalarlo, así como instrucciones para programar la ejecución automática del script y advertencias de seguridad.
