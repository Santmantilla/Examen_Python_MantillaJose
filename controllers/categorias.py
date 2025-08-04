import os
import config as config
import controllers.mainmenu
import utils.corefiles
import utils.screenControllers
import utils.validateData
from tabulate import tabulate
import controllers as controllers

opcionesCategorias = ['Agregar categoria','Ver categorias','Actualizar categoria','Eliminar categoria', 'Regresar al menu principal']

def agregar_categoria():
    while True:
        utils.screenControllers.limpiar_pantalla()
        categorias = utils.corefiles.readJson(config.DB_FILE_CATEGORIAS)

        if not isinstance(categorias,list):
            categorias = []

        nombre_categoria = utils.validateData.validarTexto('Ingrese el nombre de la categoria: ')
        descripcion = utils.validateData.validarTexto('Ingrese una descripcion: ')

        for categoria in categorias:
            if (categoria['nombre_categoria'] == nombre_categoria):
                print(f"La categoria '{nombre_categoria}' ya se encuentra registrado.")
                utils.screenControllers.pausar_pantalla()
                return
    
        nueva_categoria = {
            "nombre_categoria":nombre_categoria,
            "descripcion":descripcion
        }

        categorias.append(nueva_categoria)
        utils.corefiles.writeJson(config.DB_FILE_CATEGORIAS,categorias)
        print('Categoria registrada con exito.')
        utils.screenControllers.pausar_pantalla()
        return controllers.mainmenu.mainmenu()
    
def ver_categorias():
    utils.screenControllers.limpiar_pantalla()
    categorias = utils.corefiles.readJson(config.DB_FILE_CATEGORIAS)

    if not (categorias):
        print('Aún no hay categorias registradas')
        utils.screenControllers.pausar_pantalla()
        return
    
    tabla = []
    print('LISTA DE CATEGORIAS\n')
    for categoria in categorias:
        datos = [
            categoria.get('nombre_categoria'),
            categoria.get('descripcion')
        ] 
        tabla.append(datos)
    print(tabulate(tabla,headers=['CATEGORIA','DESCRIPCION'],tablefmt="fancy_grid"))
    utils.screenControllers.pausar_pantalla()
    return controllers.mainmenu.mainmenu()
    
def menu_categorias():
    while True:
        utils.screenControllers.limpiar_pantalla()
        print('Bienvenido al menu de categorias')
        print('Elija una opcion')
        for idx,opcion in enumerate(opcionesCategorias,start=1):
            print(f'{idx}. {opcion}')
        op = utils.validateData.validarEntero('Seleccione una opcion (1-5): ')
        if(op < 1 or op > len(opcionesCategorias)):
            print('Opción no válida, intente de nuevo.')
            utils.screenControllers.pausar_pantalla()
        else:
            if(op == 1):
                agregar_categoria()
            elif(op == 2):
                ver_categorias()
            elif(op == 3):
                pass
            elif(op == 4):
                pass
            else:
                return controllers.mainmenu.mainmenu()