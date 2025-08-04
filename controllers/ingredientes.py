import os
import config as config
import controllers.mainmenu
import utils.corefiles
import utils.screenControllers
import utils.validateData
from tabulate import tabulate
import controllers as controllers

opcionesIngredientes = ['Agregar ingrediente','Ver ingredientes','Actualizar ingrediente','Eliminar ingrediente', 'Regresar al menu principal']

def agregar_ingrediente():
    while True:
        ingredientes = utils.corefiles.readJson(config.DB_FILE_INGREDIENTES)

        if not isinstance(ingredientes,list):
            ingredientes = []

        nombre_ingrediente = utils.validateData.validarTexto('Ingrese el nombre del ingrediente: ')
        descripcion = utils.validateData.validarTexto('Ingrese una descripcion: ')
        precio = utils.validateData.validarEntero('Ingrese el costo: ')
        stock = utils.validateData.validarEntero('Ingrese el stock que hay: ')

        for ingrediente in ingredientes:
            if (ingrediente['nombre_ingrediente'] == nombre_ingrediente):
                print(f"El ingrediente '{nombre_ingrediente}' ya se encuentra registrado.")
                utils.screenControllers.pausar_pantalla()
                return
    
        nuevo_ingrediente = {
            "nombre_ingrediente":nombre_ingrediente,
            "descripcion":descripcion,
            "precio":precio,
            "stock":stock
        }

        ingredientes.append(nuevo_ingrediente)
        utils.corefiles.writeJson(config.DB_FILE_INGREDIENTES,ingredientes)
        print('Ingrediente registrado con exito.')
        utils.screenControllers.pausar_pantalla()
        return controllers.mainmenu.mainmenu()
    
def ver_ingredientes():
    utils.screenControllers.limpiar_pantalla()
    ingredientes = utils.corefiles.readJson(config.DB_FILE_INGREDIENTES)

    if not (ingredientes):
        print('Aún no hay ingredientes registradas')
        utils.screenControllers.pausar_pantalla()
        return
    
    tabla = []
    print('LISTA DE INGREDIENTES\n')
    for ingrediente in ingredientes:
        datos = [
            ingrediente.get('nombre_ingrediente'),
            ingrediente.get('descripcion'),
            ingrediente.get('precio'),
            ingrediente.get('stock')
        ] 
        tabla.append(datos)
    print(tabulate(tabla,headers=['NOMBRE INGREDIENTE','DESCRIPCION','PRECIO','STOCK'],tablefmt="fancy_grid"))
    utils.screenControllers.pausar_pantalla()
    return controllers.mainmenu.mainmenu()
    
def menu_ingredientes():
    while True:
        utils.screenControllers.limpiar_pantalla()
        print('Bienvenido al menu de ingredientes')
        print('Elija una opcion')
        for idx,opcion in enumerate(opcionesIngredientes,start=1):
            print(f'{idx}. {opcion}')
        op = utils.validateData.validarEntero('Seleccione una opcion (1-5): ')
        if(op < 1 or op > len(opcionesIngredientes)):
            print('Opción no válida, intente de nuevo.')
            utils.screenControllers.pausar_pantalla()
        else:
            if(op == 1):
                agregar_ingrediente()
            elif(op == 2):
                ver_ingredientes()
            elif(op == 3):
                pass
            elif(op == 4):
                pass
            else:
                return controllers.mainmenu.mainmenu()
        
    