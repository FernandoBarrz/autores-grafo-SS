"""
Utiliza las listas de colaboraciones y el archivo de la lista de nombres de IIBO

"""

from code.utils.generate_collabs_lists import generate_list_of_authors_from_pub
from code.utils.normalize_names import cap_names_raw
from code.utils.normalize_names import normalize


def generate_collabs_num(nombre_from_pub) -> list:
        
    autores_x_colab = []
    
    
    for author_collab in nombre_from_pub:
        # Lista de apellidos, nombres (sin acentos ni guines) - turn to Set()
        collab_name_list = set(normalize(author_collab).split(" "))       
        
        for autor_name in cap_names_raw():
            collab_match = collab_name_list.intersection(autor_name.split(" "))
            
            if len(collab_match) >= 2: # número de coincidencias minimas para hacer match
                
                autores_x_colab.append(autor_name)
                break
            
    
    return autores_x_colab
    

if __name__ == '__main__':
    
    print("Not main app, run: python3 main_en.py")



