
from pprint import pprint


def indexer_dic():
    indexed_names = {}
    with open('../../input/nombre-investigadores.txt', 'r') as nombres_inv:
        lista_nombres_raw = list(nombres_inv.readlines())
        lista_nombres_capitalized = []
        for index, nombre in enumerate(lista_nombres_raw):
            # Elimina salto de linea al final
            indexed_names[index] = nombre[:-1]
    return indexed_names

# TODO agregar a estadisticas
print(len(indexer_dic()))

# TODO agregar a las operaciones básicas
pprint(indexer_dic().get(0))

#print(indexer_dic().values())
pprint(indexer_dic())


        