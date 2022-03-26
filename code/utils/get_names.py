

def mostrar_nombre_investigadores():
    ''' 
        Muestra la lista de nombres de los investigadores.
        Params: N/A
        Return: Imprime en consola los nombres
    '''

    with open('./input/nombre-investigadores.txt', 'r') as nombre_autores:
        print('\n\n')
        for indice, nombre in enumerate(nombre_autores):
            print(f' {indice + 1} - {nombre[:-1]}')






if __name__ == '__main__':
    print("Not main app, run: python3 main.py")




