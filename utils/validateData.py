import utils.screenControllers as screen

#Esta funcion valida si el valor ingresado es un numero entero
def validarEntero(msg:str)->int:
    while True:
        try:
            mensaje = int(input(msg))
            return mensaje
        except ValueError:
            print('Ingrese un valor correcto.')
            screen.pausar_pantalla()
        
#Esta funcion valida si el valor ingresado es un numero float       
def validarDecimal(msg:str)->float:
    while True:
        try:
            mensaje = float(input(msg))
            return mensaje
        except ValueError:
            screen.limpiar_pantalla()
            print('Ingrese un valor correcto.')
            screen.pausar_pantalla()


#Esta funcion valida si el valor ingresado es un string 
def validarTexto(msg):
    while True:
        mensaje = input(msg).strip().capitalize()
        valido = True
        for caracter in mensaje:
            if not (caracter.isalpha() or caracter.isspace()):
                valido = False
                break
        
        if (valido):
            return mensaje
        else:
            screen.limpiar_pantalla()
            print('Ingrese un valor correcto.')
            screen.pausar_pantalla()


def validarAlfanumerico(msg):
    while True:
        mensaje = input(msg).strip().capitalize()
        valido = True
        for caracter in mensaje:
            if not (caracter.isalnum):
                valido = False
                break        
        if (valido):
            return mensaje
        else:
            screen.limpiar_pantalla()
            print('Ingrese un valor correcto.')
            screen.pausar_pantalla()