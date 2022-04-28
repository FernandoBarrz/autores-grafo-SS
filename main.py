import os
from pprint import pprint
from code.utils.get_names import mostrar_nombre_investigadores
from code.utils.parse_bd import print_txt_to_lists, parse_txt_to_lists
from code.utils.generate_graph import show_graph_cli
from code.utils.generate_statistics import show_statistics_cli





menu_options = {
    1: 'Ver nombre de los investigadores',
    2: 'Mostrar base de datos', 
    3: 'Mostrar grafó',
    4: 'Mostrar estadísticas',
    5: 'Salir del programa'
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
            bulk = parse_txt_to_lists()
            pprint(bulk)
            print('Total length: ',len(bulk), end='\n')

        elif opcion == 3:
            #os.system('clear || cls')
            show_graph_cli()
        elif opcion == 4:
            show_statistics_cli()
        elif opcion == 5 or opcion == 'q':
            #os.system('clear || cls')
            print("Saliendo del programa...")
            break
        else:
            print('Error al seleccionar opción.')
            os.system('clear || cls')



    



























