
from pprint import pprint


def indexer_dic():
    indexed_names = {}
    with open('./nombre-investigadores.txt', 'r') as nombres_inv:
        lista_nombres_raw = list(nombres_inv.readlines())
        lista_nombres_capitalized = []
        for index, nombre in enumerate(lista_nombres_raw):
            # Elimina salto de linea al final
            indexed_names[index] = nombre[:-1]
    return indexed_names




if __name__ == '__main__':
    print(indexer_dic())
    print("Not main app, run: python3 main_en.py")
        