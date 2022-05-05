import os
from pprint import pprint
from code.utils.get_names import mostrar_nombre_investigadores
from code.utils.parse_bd import parse_txt_to_lists
from code.graph.show_graph_cli import show_graph_console
from code.graph.show_graph_visually import show_graph_image
from code.utils.generate_statistics import show_statistics_cli



menu_options = {
    1: 'Show researchers\'s names',
    2: 'Show data record', 
    3: 'Show graph (CLI)',
    4: 'Show graph (Visually and open Image)',
    5: 'Show statistics',
    6: 'Exit'
}

def print_menu():
    print('CLI to generate a (undirected / weighted) graph that represents collaborations between researchers at the institute.\n')
    print('Option menu: \n Type a number.\n')
    for key in menu_options.keys():
        print(key, '--', menu_options[key])




    
if __name__ == '__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choise: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            mostrar_nombre_investigadores()
        elif option == 2:
            bulk = parse_txt_to_lists()
            pprint(bulk)
            print('Total length: ',len(bulk), end='\n')
        elif option == 3:
            show_graph_console()
        elif option == 4:
            show_graph_image()
        elif option == 5:
            show_statistics_cli()
        elif option == 6:
            break
        else:
            print('Invalid option. Please enter a number between 1 and 5.')
