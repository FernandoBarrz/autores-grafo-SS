import os
from pprint import pprint
from code.utils.get_names import mostrar_nombre_investigadores
from code.utils.parse_bd import parse_txt_to_lists
from code.graph.show_graph_cli import show_graph_console
from code.utils.generate_collabs_lists import generate_list_of_authors_from_pub
from code.utils.generate_collabs_num import generate_collabs_num
from code.graph.generate_graph import generate_graph_data
from code.graph.generate_graph import create_graph
from code.utils.generate_statistics import show_statistics_cli
from code.graph.show_graph_cli import show_graph_console

# **** Quitar el comentario para abilitar la libreria
#from code.graph.show_graph_visually import show_graph_image

menu_options = {
    1: 'Ver nombre de los investigadores',
    2: 'Mostrar base de datos', 
    3: 'Mostrar grafó en CLI (Texto)',
    4: 'Generar imagen con los datos del grafó',
    5: 'Mostrar número total colaboraciones por investigador',
    6: 'Salir del programa'
}

def mostrar_menu():
    print('\nSistema para mostrar un grafo con peso no dirigido que represanta las colaboraciones entre investigadores del instituto\n')
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
            mostrar_nombre_investigadores()

        elif opcion == 2:
            bulk = parse_txt_to_lists()
            pprint(bulk)
            print('Tamaño total de registros: ',len(bulk), end='\n')

        elif opcion == 3:
            show_graph_console()

        elif opcion == 4:
            try:
                show_graph_image()
            except:
                print("\nDebe instalar las librarias de terceros y modificar los módulos del programa. (Mire la documentación)")

        elif opcion == 5:
            show_statistics_cli()
            
        elif opcion == 6 or opcion == 'q' or opcion == 's':
            
            pprint("Saliendo del programa...")
            break

        else:
            print('\nError al seleccionar opción.')
            



    



























