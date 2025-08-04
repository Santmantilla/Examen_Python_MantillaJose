## Este es un proyecto hecho en Python para gestionar el inventario de un restaurante que van a incluir ingredientes, hamburguesas, categorias y chefs. Es desarrollado como parte del examen final del skill de Python, donde se busca programar un CRUD en consola haciendo practica de lectura/escritura de archivos JSON, uso de funciones, validaciones y estructura de carpetas en Python.

## Que hace?
**El programa permite:**

- Añadir un nuevo elemento, sea ingredientes, hamburguesas, categorias o chefs.
- Ver los elementos agregados sea ingredientes, hamburguesas, categorias o chefs.
- Editar un elemento ya sea sea ingredientes, hamburguesas, categorias o chefs.

**Estructura del proyecto**
- controllers/: Aca van las funciones principales del menu, las cuales contiene todas las funciones logicas del funcionamiento del programa.
- data/: Aca estaran almacenados todos los archivos JSON que como informacion tendran ingredientes, hamburguesas, categorias o chefs.
- utils/: Aca estan las funciones que ayudan a validar los datos y al manejo de los archivos.
- app.py: Este es el archivo principal que nos ayuda a que el programa pueda ejecutarse.
- config.py: Este archivo tendra almacenado las rutas de los archivos JSON.

**Estructura del proyecto - Explicacion**
**controllers/**

- mainmenu.py: Este archivo es el que controla todas las funcionalidades del menu principal, es decir, de las opciones que tiene el usuario para escoger.
- ingredientes.py,hamburguesas.py,categorias.py,chefs.py: Estos archivos son los que van permites que se pueda registrar y mostrar elementos de cada seccion, sea ingredientes, hamburguesas, categorias o chefs.

**data/**

categorias.json: Este archivo JSON almacena toda la informacion sobre las categorias agregadas
chefs.json: Este archivo JSON almacena toda la informacion sobre los chefs agregados
hamburguesas.json: Este archivo JSON almacena toda la informacion sobre las hamburguesas agregadas
ingredientes.json: Este archivo JSON almacena toda la informacion sobre los ingredientes agregados
utils/

corefiles.py: Este archivo contiene las funciones para leer, escribir, actualizar y eliminar datos en archivos JSON.
screenControllers.py: Este archivo tienes las funciones para pausar la consola o limpiar la consola.
validateData.py: Este archivo valida la entrada de los datos que ingresa el usuario. Valida si es entero, decimal o string.