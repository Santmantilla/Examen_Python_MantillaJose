import os
import config as config
import controllers.mainmenu
import utils.corefiles
import utils.screenControllers
import utils.validateData
import controllers as controllers
from tabulate import tabulate

opcionesChefs = ['Agregar chef','Ver chefs','Actualizar chef','Eliminar chef', 'Regresar al menu principal']

def agregar_chef():
    while True:
        utils.screenControllers.limpiar_pantalla()
        chefs = utils.corefiles.readJson(config.DB_FILE_CHEFS)

        if not isinstance(chefs,list):
            chefs = []

        nombre_chef = utils.validateData.validarTexto('Ingrese el nombre del ingrediente: ')
        especialidad = utils.validateData.validarTexto('Ingrese su especialidad: ')
        id_chef = utils.validateData.validarEntero('Ingrese el ID del chef: ')
    
        nuevo_chef = {
            "nombre_chef":nombre_chef,
            "especialidad":especialidad,
            "id_chef":id_chef
        }

        chefs.append(nuevo_chef)
        utils.corefiles.writeJson(config.DB_FILE_CHEFS,chefs)
        print('Chef registrado con exito.')
        utils.screenControllers.pausar_pantalla()
        return controllers.mainmenu.mainmenu()
    
def ver_chefs():
    utils.screenControllers.limpiar_pantalla()
    chefs = utils.corefiles.readJson(config.DB_FILE_CHEFS)

    if not (chefs):
        print('Aún no hay ingredientes registradas')
        utils.screenControllers.pausar_pantalla()
        return
    
    tabla = []
    print('LISTA DE CHEFS\n')
    for chef in chefs:
        datos = [
            chef.get('nombre_chef'),
            chef.get('especialidad'),
            chef.get('id_chef')
        ] 
        tabla.append(datos)
    print(tabulate(tabla,headers=['NOMBRE CHEF','ESPECIALIDAD','ID'],tablefmt="fancy_grid"))
    utils.screenControllers.pausar_pantalla()
    return controllers.mainmenu.mainmenu()
    
def menu_chefs():
    while True:
        utils.screenControllers.limpiar_pantalla()
        print('Bienvenido al menu de chefs')
        print('Elija una opcion')
        for idx,opcion in enumerate(opcionesChefs,start=1):
            print(f'{idx}. {opcion}')
        op = utils.validateData.validarEntero('Seleccione una opcion (1-5): ')
        if(op < 1 or op > len(opcionesChefs)):
            print('Opción no válida, intente de nuevo.')
            utils.screenControllers.pausar_pantalla()
        else:
            if(op == 1):
                agregar_chef()
            elif(op == 2):
                ver_chefs()
            elif(op == 3):
                pass
            elif(op == 4):
                pass
            else:
                return controllers.mainmenu.mainmenu()