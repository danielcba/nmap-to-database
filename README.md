## Propósito del Script

Este script automatiza el proceso de escaneo de una red para identificar dispositivos conectados y los servicios que están ejecutando, y luego almacena estos resultados en una base de datos para su análisis y consulta posterior. Es útil para administradores de red y profesionales de seguridad informática que necesitan monitorizar y gestionar la infraestructura de red de manera eficiente.

### Funciones Clave del Script

1. **Escaneo de Red**:

   - Utiliza `nmap`, una poderosa herramienta de escaneo de redes, para buscar todos los dispositivos en una red específica y detectar los servicios y versiones de software que están ejecutando.
   - El escaneo abarca un rango de direcciones IP y utiliza técnicas avanzadas para identificar servicios activos y versiones de software con gran precisión.

2. **Generación de Resultados**:

   - Los resultados del escaneo se guardan en un archivo en formato CSV (valores separados por comas), que facilita la organización y el análisis de los datos recolectados.

3. **Almacenamiento en Base de Datos**:
   - Conecta a una base de datos MariaDB y carga los resultados del escaneo en una tabla específica.
   - Almacenar los resultados en una base de datos permite consultas rápidas y eficientes, y facilita la integración con otras herramientas de análisis y reporte.

### Beneficios del Script

- **Automatización**: El script automatiza todo el proceso, desde el escaneo hasta el almacenamiento de datos, ahorrando tiempo y reduciendo errores humanos.
- **Monitorización Continua**: Se puede ejecutar periódicamente para mantener una visión actualizada de la red, ayudando a detectar cambios no autorizados o problemas potenciales.
- **Análisis de Seguridad**: Ayuda a identificar servicios y versiones de software en la red que podrían ser vulnerables, facilitando la gestión de parches y actualizaciones de seguridad.
- **Inventario de Red**: Proporciona un inventario detallado de todos los dispositivos y servicios en la red, útil para la gestión de activos y planificación de capacidad.

### Uso Típico

1. **Administradores de Red**: Pueden utilizar el script para obtener una visión general de la infraestructura de red, identificar dispositivos y servicios, y mantener un inventario actualizado.
2. **Profesionales de Seguridad**: Pueden usar los datos para realizar evaluaciones de seguridad, identificar posibles vulnerabilidades y planificar acciones correctivas.
3. **Auditores**: Pueden emplear el script como parte de auditorías de red para verificar la conformidad con políticas y normativas de seguridad.

### Consideraciones de Seguridad

- **Manejo de Credenciales**: Es importante no almacenar credenciales directamente en el código. Se recomienda usar variables de entorno o archivos de configuración seguros.
- **Permisos y Accesos**: Asegurarse de que solo personal autorizado pueda ejecutar el script y acceder a los resultados almacenados.

---

Este script es una herramienta poderosa y versátil para la gestión y seguridad de redes, proporcionando información crítica de manera automatizada y eficiente.

---

### Archivo `requirements.txt`

Este archivo especifica las dependencias necesarias para ejecutar el script de Python.

```
python-nmap
mysql-connector-python
```

### Líneas SQL para la creación de la base de datos y la tabla

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

---

## Instalación de Dependencias

1. Crear y activar un entorno virtual (opcional pero recomendado):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Instalar las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
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

---

## Programación de la Ejecución del Script

Si deseas que el script se ejecute automáticamente cada cierto tiempo, puedes configurarlo como una tarea programada (cron job) en tu sistema operativo. A continuación, se explica cómo hacerlo.

### Configuración de Crontab

1. Abre el editor de crontab para el usuario actual:

   ```bash
   crontab -e
   ```

2. Añade la siguiente línea al final del archivo para ejecutar el script cada 2 minutos:

   ```bash
   */2 * * * * /usr/bin/python3 /home/username/base-nmap/nmap-to-database.py
   ```

   Esta línea programa la ejecución del script `nmap-to-database.py` cada 2 minutos. Si deseas cambiar la frecuencia, ajusta el primer campo (\*/2) según tus necesidades. Aquí hay algunos ejemplos:

   - Cada 5 minutos:
     ```bash
     */5 * * * * /usr/bin/python3 /home/username/base-nmap/nmap-to-database.py
     ```
   - Cada hora:
     ```bash
     0 * * * * /usr/bin/python3 /home/username/base-nmap/nmap-to-database.py
     ```
   - Todos los días a las 3 AM:
     ```bash
     0 3 * * * /usr/bin/python3 /home/username/base-nmap/nmap-to-database.py
     ```

### Guardar y Salir

- En el editor de crontab, guarda los cambios y cierra el editor. En `nano`, por ejemplo, presiona `CTRL+O` para guardar y `CTRL+X` para salir.

### Verificación

- Para verificar que la tarea se ha añadido correctamente, puedes listar las tareas programadas:
  ```bash
  crontab -l
  ```

### Nota de Seguridad

Asegúrate de que el script `nmap-to-database.py` tenga permisos de ejecución y que el usuario que configura el cron job tenga los permisos necesarios para ejecutar el script y acceder a la base de datos.

### Resultado

![image](https://github.com/danielcba/nmap-to-database/assets/157246808/44615c4f-6345-41e1-9d04-6639c15448b6)


---
