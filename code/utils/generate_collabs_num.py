"""
Utiliza las listas de colaboraciones y el archivo de la lista de nombres de IIBO

"""

from code.utils.generate_collabs_lists import generate_list_of_authors_from_pub
from code.utils.normalize_names import cap_names_raw
from code.utils.normalize_names import normalize


def generate_collabs_num(nombre_from_pub) -> list:
    
    
    
    
    autores_x_colab = []
    count_collabs = 0
    
    for author_collab in nombre_from_pub:
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
                autores_x_colab.append(autor_name)
                break
            
    
    return autores_x_colab
    
    
    
    

if __name__ == '__main__':
    
    print("Not main app, run: python3 main_en.py")



