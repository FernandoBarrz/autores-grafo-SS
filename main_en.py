import os
from pprint import pprint
from code.utils.get_names import mostrar_nombre_investigadores
from code.utils.parse_bd import parse_txt_to_lists
from code.utils.generate_graph import show_graph_cli
from code.utils.generate_statistics import show_statistics_cli



menu_options = {
    1: 'Show researchers\'s names',
    2: 'Show data record', 
    3: 'Show graph',
    4: 'Show statistics',
    5: 'Exit'
}

def print_menu():
    print('CLI to generate an undirected weighted graph that represents collaborations between researchers at the institute.\n')
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
            print('Total length: ', end='\n')
        elif option == 3:
            show_graph_cli()
        elif option == 4:
            show_statistics_cli()
        elif option == 5:
            break
        else:
            print('Invalid option. Please enter a number between 1 and 5.')
