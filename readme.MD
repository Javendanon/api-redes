# API Rest en python 3.7


## Instalación
Antes de crear el entorno virtual asegurarse de descargar 
[Python 3.7](https://www.python.org/downloads/) desde la web oficial.
Crear un entorno virtual con venv o conda con la versión de python 3.7, instalar mediante pip el módulo flask

`pip install flask`

## Ejecución

Para ejecutar la api en local se debe ejecutar el siguiente comando desde la terminal en el directorio del repositorio

`python main.py`

y esperar a que cargue, posteriormente en la consola se imprimirá una dirección de tipo 

`http://localhost:puerto`

el puerto puede variar dependiendo del equipo, la api se compone de 2 métodos 

### VerificaRut 
Servicio POST que calcula y verifica el rut ingresado de tipo "12345678-9", responde en formato JSON y retorna un objeto con un mensaje que informa al cliente de lo sucedido y"ok" -> True si la petición fué realizada correctamente en caso contrario, un "ok"-> False.
Para utilizar este servicio es necesario realizar una petición HTTP de tipo POST y que en el body de la petición se incorpore un atributo "rut" con el valor deseado en la siguiente ruta.
`http://localhost:puerto/verificaRut`

tambien es posible realizar la petición al host que aloja esta API en caso de no poder realizar la instalación.

`http://javendanon.pythonanywhere.com/verificaRut`

### NombrePropio

Servicio POST que aplica formato proper case el nombre, apellido materno, apellido paterno y género que sea ingresado independiente del formato inicial, responde en formato JSON y retorna un objeto con un mensaje que informa al cliente de lo sucedido y "ok" -> True si la petición fué realizada correctamente en caso contrario "ok"-> False.

Para utilizar este servicio es necesario realizar una petición HTTP de tipo POST y que en el body se incorporen los siguientes atributos:

 1. name
 2. apellido_p
 3. apellido_m
 4. gender

con los valores deseados en la siguiente ruta:

`http://localhost:puerto/nombrePropio` 

tambien es posible realizar la petición al host que aloja esta API en caso de no poder realizar la instalación.

`http://javendanon.pythonanywhere.com/nombrePropio`
