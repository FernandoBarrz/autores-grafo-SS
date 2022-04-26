import os
from code.utils.get_names import mostrar_nombre_investigadores


def mostrar_base_datos():
    print('base de datos dasdasd')
    print('fewfwe\n' * 3)
def mostrar_documentacion():
    print('documentacion')
    print('fewfwe\n' * 3)
def mostrar_grafo():
    print('grafooo')
    print('fewfwe\n' * 3)




menu_options = {
    1: 'Ver nombre de los investigadores',
    2: 'Mostrar base de datos', 
    3: 'Mostrar grafó',
    4: 'Salir del programa'
}

def mostrar_menu():
    print('Sistema para mostrar un grafo con peso no dirigido que represanta las colaboraciones entre investigadores\n')
    print('Menú de opciones: \n')
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


if __name__ == '__main__':
    while True:
        mostrar_menu()
        opcion: str = ''
        try:
            opcion = int(input('\nIngrese una opción: \t'))
        except:
            print('Error al ingresar una opción')

        if opcion == 1:
            #os.system('clear || cls')
            mostrar_nombre_investigadores()

        elif opcion == 2:
            #os.system('clear || cls')
            mostrar_base_datos()

        elif opcion == 3:
            #os.system('clear || cls')
            mostrar_grafo()

        elif opcion == 4 or opcion == 'q':
            #os.system('clear || cls')
            print("Saliendo del programa...")
            break
        else:
            print('Error al seleccionar opción.')
            os.system('clear || cls')
            continue



    



























