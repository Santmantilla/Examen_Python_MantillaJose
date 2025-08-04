import os
import controllers.categorias
import controllers.chefs
import controllers.hamburguesas
import controllers.ingredientes
import utils as utils
import utils.screenControllers
import controllers as controllers

opciones = ['Ingredientes','Categorias','Chefs','Hamburguesas','Salir']

def mainmenu():
    while True:
        utils.screenControllers.limpiar_pantalla()
        print('Bienvenido al menu principal')
        print('¿A que apartado desea acceder?')
        for idx,opcion in enumerate(opciones,start=1):
            print(f'{idx}. {opcion}')
        op = utils.validateData.validarEntero('Seleccione una opcion (1-5): ')
        if(op < 1 or op > len(opciones)):
            print('Opción no válida, intente de nuevo.')
            utils.screenControllers.pausar_pantalla()
        else:
            if(op == 1):
                controllers.ingredientes.menu_ingredientes()
            elif(op == 2):
                controllers.categorias.menu_categorias()
            elif(op == 3):
                controllers.chefs.menu_chefs()
            elif(op == 4):
                controllers.hamburguesas.menu_hamburguesas()
            else:
                break