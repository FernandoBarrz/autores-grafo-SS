import os

def mostrar_nombre_investigadores():
    print('nombres investigadores sdasdasda -......')
def mostrar_base_datos():
    print('base de datos dasdasd')
def mostrar_documentacion():
    print('documentacion')
def mostrar_grafo():
    print('grafooo')

flag = 1
while flag == 1:
    print('Sistema para mostrar un grafo con peso dirigido que represanta las colaboraciones\n')
    print('Menú de opciones: \n Escriba un número')
    opcion_input = input(f'1 - Ver nombre de los investigadores \n2 - mostrar base de datos \n3 - Ver documentación \n4 - Mirar grafo. \n5 / q - Salir del programa \n\nNúmero de opción:\t')
    if bool(opcion_input) == False:
        print('Ingrese una opción valida')
        continue
    elif opcion_input == '1':
        mostrar_nombre_investigadores()
        os.system('cls||clear')

    elif opcion_input == '2':
        mostrar_base_datos()
        os.system('cls||clear')

    elif opcion_input == '3':
        mostrar_documentacion()
        os.system('cls||clear')

    elif opcion_input == '4':
        mostrar_grafo()
        os.system('cls||clear')

    elif opcion_input == 'q' or opcion_input == '5':
        print("Saliendo del programa...")
        os.system('cls||clear')
        flag = 0

    else:
        print('Escoja una opción valida.')
        os.system('cls||clear')
        continue





























