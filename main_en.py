import os
from code.utils.get_names import mostrar_nombre_investigadores


def mostrar_base_datos():
    print('Show data record')
def mostrar_documentacion():
    print('Show documentation')
def mostrar_grafo():
    print('Show graph')


menu_options = {
    1: 'Show researchers\'s names',
    2: 'Show data record', 
    3: 'Show graph',
    4: 'Exit'
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
            mostrar_base_datos()
        elif option == 2:
            mostrar_base_datos()
        elif option == 3:
            mostrar_grafo()
        elif option == 4:
            break
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
    