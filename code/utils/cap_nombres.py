from pprint import pprint


def normalize(s):
    ''' Reemplaza las letras con tildes de una cadena de texto
        Args: 
            El caracter a reemplzar
        Return:
            Catacter sin tilde
    '''
    replacements = (
        ('á', 'a'),
        ('é', 'e'),
        ('í', 'i'),
        ('ó', 'o'),
        ('u', 'u')
    )
    for a, b in  replacements:
        s = s.replace(a, b)
    return s


# TODO quitar el \n de las listas

with open('../../input/nombre-investigadores.txt', 'r') as nombres_inv:
    lista_nombres_raw = list(nombres_inv.readlines())
    lista_nombres_capitalized = []
    for nombre in lista_nombres_raw:
        lista_nombre = nombre.split(' ')

        temp_nombre = lista_nombre[1:-1]
        temp_nombre = "-".join(temp_nombre)
        temp_nombre = temp_nombre.title()

        pprint(temp_nombre)