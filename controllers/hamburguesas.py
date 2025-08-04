import os
import config as config
import controllers.mainmenu
import utils.corefiles
import utils.screenControllers
import utils.validateData
import controllers as controllers
from tabulate import tabulate

opcionesHamburguesas = ['Agregar hamburguesa','Ver hamburguesas','Actualizar hamburguesa','Eliminar hamburguesa', 'Regresar al menu principal']

def agregar_hamburguesa():
    while True:
        utils.screenControllers.limpiar_pantalla()
        hamburguesas = utils.corefiles.readJson(config.DB_FILE_HAMBURGUESAS)
        categorias = utils.corefiles.readJson(config.DB_FILE_CATEGORIAS)
        ingredientes = utils.corefiles.readJson(config.DB_FILE_INGREDIENTES)
        chefs = utils.corefiles.readJson(config.DB_FILE_CHEFS)

        if not isinstance(hamburguesas,list):
            hamburguesas = []

        nombre_hamburguesa = utils.validateData.validarTexto('Ingrese el nombre de la hamburguesa: ')
        nombre_categoria = utils.validateData.validarTexto('Ingrese el nombre de la categoria: ')

        encontradosCategorias = []

        for categoria in categorias:
            if (nombre_categoria == categorias['nombre_categoria']):
                encontradosCategorias.append(nombre_categoria)
                utils.screenControllers.pausar_pantalla()
            else:
                print(f"La categoria '{nombre_categoria}' no se encuentra registrada.")
                utils.screenControllers.pausar_pantalla
                return
        
        lista_ingredientes_ingresados = []
        for i in range (4):
            nombre_ingrediente =  utils.validateData.validarTexto(f'Ingrese el ingrediente {i+1}: ')
            lista_ingredientes_ingresados.append(nombre_ingrediente)

                
        precio = utils.validateData.validarEntero('Ingrese el valor de la hamburguesa: ')

        nombre_chef = utils.validateData.validarTexto('Ingrese el nombre del chef: ')
        for chef in chefs:
            if(nombre_chef != chef['nombre_chef']):
                print('Este chef no se encuentra registrado')
                return
 
        nueva_hamburguesa = {
            "nombre_hamburguesa":nombre_hamburguesa,
            "nombre_categoria":nombre_categoria,
            "lista_ingredientes":lista_ingredientes_ingresados,
            "precio":precio,
            "nombre_chef":nombre_chef
        }

        hamburguesas.append(nueva_hamburguesa)
        utils.corefiles.writeJson(config.DB_FILE_HAMBURGUESAS,hamburguesas)
        print('Hamburguesa registrada con exito.')
        utils.screenControllers.pausar_pantalla()
        return controllers.mainmenu.mainmenu()
    
def ver_hamburguesas():
    utils.screenControllers.limpiar_pantalla()
    hamburguesas = utils.corefiles.readJson(config.DB_FILE_HAMBURGUESAS)

    if not (hamburguesas):
        print('Aún no hay ingredientes registradas')
        utils.screenControllers.pausar_pantalla()
        return
    
    tabla = []
    print('LISTA DE HAMBURGUESAS\n')
    for hamburguesa in hamburguesas:
        datos = [
            hamburguesa.get('nombre_hamburguesa'),
            hamburguesa.get('nombre_categoria'),
            hamburguesa.get('lista_ingredientes'),
            hamburguesa.get('precio'),
            hamburguesa.get('nombre_chef')
        ] 
        tabla.append(datos)
    print(tabulate(tabla,headers=['NOMBRE HAMBURGUESA','NOMBRE CATEGORIA','LISTA INGREDIENTES','PRECIO','NOMBRE CHEF'],tablefmt="fancy_grid"))
    utils.screenControllers.pausar_pantalla()
    return controllers.mainmenu.mainmenu()
    
def menu_hamburguesas():
    while True:
        utils.screenControllers.limpiar_pantalla()
        print('Bienvenido al menu de hamburguesas')
        print('Elija una opcion')
        for idx,opcion in enumerate(opcionesHamburguesas,start=1):
            print(f'{idx}. {opcion}')
        op = utils.validateData.validarEntero('Seleccione una opcion (1-5): ')
        if(op < 1 or op > len(opcionesHamburguesas)):
            print('Opción no válida, intente de nuevo.')
            utils.screenControllers.pausar_pantalla()
        else:
            if(op == 1):
                agregar_hamburguesa()
            elif(op == 2):
                ver_hamburguesas()
            elif(op == 3):
                pass
            elif(op == 4):
                pass
            else:
                return controllers.mainmenu.mainmenu()