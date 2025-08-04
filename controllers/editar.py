import controllers as controllers
import config as config
import utils as utils
import utils.corefiles
import utils.screenControllers

opcionesEditar = ['Editar ingrediente','Editar categoria','Editar chef','Editar hamburguesa','Regresar al menú principal']

def editar():
    utils.screenControllers.limpiar_pantalla()
    print('EDITAR ELEMENTO')

    ingredientes = utils.corefiles.readJson(config.DB_FILE_INGREDIENTES)
    peliculas = corefiles.readJson(DB_FILE_PELICULAS)
    musica = corefiles.readJson(DB_FILE_MUSICA)

    encontrados = []
    for libro in libros:
        libro['tipo'] = 'Libro'
        encontrados.append(libro)
    for pelicula in peliculas:
        pelicula['tipo'] = 'Pelicula'
        encontrados.append(pelicula)
    for cancion in musica:
        cancion['tipo'] = 'Musica'
        encontrados.append(cancion)

    if not (encontrados):
        print('Aún no hay elementos para editar')
        screen.pausar_pantalla()
        return

    tabla = []
    for idx, dato in enumerate(encontrados, start=1):
        if (dato['tipo'] == 'Libro'):
            fila = [idx, dato['id_libro'],dato['tipo'],dato['nombre_libro'], dato['autor'], dato['genero'], dato['valoracion']]
        elif (dato['tipo'] == 'Pelicula'):
            fila = [idx, dato['id_pelicula'],dato['tipo'],dato['nombre_pelicula'], dato['director'], dato['genero'], dato['valoracion']]
        elif (dato['tipo'] == 'Musica'):
            fila = [idx, dato['id_cancion'],dato['tipo'], dato['nombre_cancion'], dato['artista'], dato['genero'], dato['valoracion']]
        tabla.append(fila)

    print(tabulate(tabla, headers=['Indice', 'ID','Tipo','Nombre', 'Autor/Director/Artista', 'Género', 'Valoración'], tablefmt='fancy_grid'))

    seleccion = validarDatos.validarEntero('Seleccione la opcion que desee editar: ')
    if (seleccion < 1 or seleccion > len(encontrados)):
        print('Selección inválida')
        screen.pausar_pantalla()
        return

    elemento = encontrados[seleccion - 1]

    while True:
        print('¿Que tipo de cambio deseas realizar?')
        for i,opcion in enumerate(opcionesEditar,start = 1):
            print(f'{i}. {opcion}')
        op = validarDatos.validarEntero('Seleccione la opcion: ')
        if (op < 1 or op > len(opcionesEditar)):
            print('Selección inválida')
            screen.pausar_pantalla()
        else:
            if elemento['tipo'] == 'Libro':
                id_key = 'id_libro'
                filename = DB_FILE_LIBROS
            elif elemento['tipo'] == 'Pelicula':
                id_key = 'id_pelicula'
                filename = DB_FILE_PELICULAS
            elif elemento['tipo'] == 'Musica':
                id_key = 'id_cancion'
                filename = DB_FILE_MUSICA

        nuevos_datos = {}

        if (op == 1):
            campo = {
                'Libro': 'nombre_libro',
                'Pelicula': 'nombre_pelicula',
                'Musica': 'nombre_cancion'
            }[elemento['tipo']]
            nuevos_datos[campo] = validarDatos.validarTexto('Nuevo título: ')
        elif (op == 2):
            campo = {
                'Libro': 'autor',
                'Pelicula': 'director',
                'Musica': 'artista'
            }[elemento['tipo']]
            nuevos_datos[campo] = validarDatos.validarTexto(f'Nuevo {campo}: ')
        elif (op == 3):
            nuevos_datos['genero'] = validarDatos.validarTexto('Nuevo género: ')
        elif op == 4:
            nuevos_datos['valoracion'] = validarDatos.validarEntero('Nueva valoración (1-10): ')
        else:
            return mainmenu.main_menu()

        corefiles.updateJson(filename, id_key, elemento[id_key], nuevos_datos)
        print(f'Se actualizo correctamente.')
        screen.pausar_pantalla()
        break