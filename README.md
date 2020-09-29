# PROYECTO 1 - SOPES 1

Proyecto 1 sistemas operativos
Primer semestre del 2020

## SERVIDOR A Y B
La configuración para ambos servidores es la misma, debe instalarse cualquier distribución de Linux y deben ser máquinas virtuales del proveedor de servicios de computación en la nube a su elección. 

- Se solicita lo siguiente:

### Módulos del Kernel
Deben programarse dos módulos, estos consultarán el porcentaje de memoria principal (RAM) utilizado en el servidor y el porcentaje de uso de CPU.

### Bases de Datos
Se debe implementar una base de datos NoSQL mediante un contenedor de Docker. 
El motor de base de datos a utilizar será MongoDB.

### API REST en Python
Se debe programar una API REST en Python, la ejecución de esta se realizará
dentro de un contenedor de Docker.

## DESCRIPCION
La API consultará la información de la base de datos y los archivos generados por los módulos cargados previamente, si otros servidores o servicios necesitan información sobre el rendimiento puede consultarlo a través de peticiones a esta API. 

Para iniciarse ambos contenedores debe utilizarse Docker Compose.