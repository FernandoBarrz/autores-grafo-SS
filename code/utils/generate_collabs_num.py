"""
Utiliza las listas de colaboraciones y el archivo de la lista de nombres de IIBO

"""

from enum import auto
from itertools import count
from posixpath import split
from code.utils.generate_collabs_lists import generate_list_of_authors_from_pub
from code.utils.normalize_names import cap_names_raw
from code.utils.normalize_names import normalize


def generate_collabs_num() -> int:
    collabs_list_raw = generate_list_of_authors_from_pub()
    a = collabs_list_raw[1]
    b = {}
    c = []
    count_collabs = 0
    test = []
    for author_collab in a:
        # Lista de apellidos, nombres (sin acentos ni guines) - turn to Set()
        collab_name_list = set(normalize(author_collab).split(" "))
        
        #print(f"dentro del PRIMER for: {collab_name_list}")
        autor_names_list = []       
        
        for autor_name in cap_names_raw():
            
            #print(f"dentro del SEGUNDO for: {autor_name}")
            collab_match = collab_name_list.intersection(autor_name.split(" "))
            #print(f"dentro del match ->  {collab_match}")
            if len(collab_match) >= 2: # número de coincidencias minimas para hacer match
                count_collabs += 1
                c.append(collab_match)
                test.append(autor_name)
                break
                

    
    
    #print(collab_name_list)
    print(a)
    print(count_collabs)
    print(c)
    print(test)
    #print(c)
    # for colab_list in collabs_list_raw:
    #     for autor_colab in colab_list:
    #         print(normalize(autor_colab))
        #print( f"TYPEEEEE -> {type(colab_list)} - LISTA -> {colab_list}")
        #for autor_in_collab in colab_list:
        
        
#nombre_cumpleto = ["memo", "leticia", "rocha", "zavaleta", 'paco']

#nombre_colab = ['rocha', 'zavaleta', 'leticia']


#for nombre in nombre_cumpleto:
#  if nombre in nombre_colab:
#    print(f'{nombre} esta en bi')
#  else:
#    print(f'{nombre} NOOO esta en bi')


if __name__ == '__main__':
    
    print("Not main app, run: python3 main_en.py")



