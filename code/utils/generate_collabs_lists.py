'''
    Genera una lista de listas que representan las colaboraciones con los autores de cada publicación
'''

from pprint import pprint

from code.utils.parse_bd import parse_txt_to_lists
from code.utils.parse_bd import parse_txt_to_lists

#from parse_bd import parse_txt_to_lists

def generate_list_of_authors_from_pub():
    """
    Genera una lista de listas que contienen los nombres pertenecientes a los autores de publicaciones
    args: Lista de Listas con datos de publicaciones sin procesar. (parse_txt_to_lists)
    return: [str, str, str, ...]
    """
    raw_data = parse_txt_to_lists()
    
    collabs_au_form_pub = []
    for chunk_pub_data in raw_data:
        temp_list = []
        for list_of_data in chunk_pub_data:
            autores_index = list_of_data.find("AU") or list_of_data.find("FAU")
 
            if autores_index and len(list_of_data[autores_index:]) > 3:
                temp_list.append(list_of_data[autores_index + 5:-1])
     
    
        collabs_au_form_pub.append(temp_list)

    return collabs_au_form_pub


if __name__ == '__main__':
    print(generate_list_of_authors_from_pub())
    print(len(generate_list_of_authors_from_pub()))
    print("Not main app, run: python3 main_en.py")