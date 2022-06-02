"""
Utiliza las listas de colaboraciones y el archivo de la lista de nombres de IIBO

"""

from code.utils.generate_collabs_lists import generate_list_of_authors_from_pub



def generate_collabs_num() -> int:
    collabs_list_raw = generate_list_of_authors_from_pub()
    
    for colab_list in collabs_list_raw:
        print(type(colab_list))
        print(f"TYPEEEEE -> {type(colab_list)} - LISTA -> {colab_list}")
        













if __name__ == '__main__':
    
    print("Not main app, run: python3 main_en.py")



