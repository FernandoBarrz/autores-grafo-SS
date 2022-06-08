


from code.graph.graph.graph import Graph

from code.utils.normalize_names import cap_names_raw
from code.utils.generate_collabs_lists import generate_list_of_authors_from_pub
from code.utils.generate_collabs_num import generate_collabs_num


def generate_graph_data():
    """
    Genera una lista de listas que representan las colaboraciones entre autores
    cada una de las listas internas representa una colaboración entre esos autores.
    """
    autores_raw = generate_list_of_authors_from_pub()
    data = []
    for autor in autores_raw:
        temp_data_rel = generate_collabs_num(autor)
        if temp_data_rel:
            data.append(temp_data_rel) 
    return data
    



def create_graph():
    """
    Llama a la clase Graph para asignarle valores
    """
    
    graph = Graph(directed=False) # Graph(directed=false) for undirected graph
    

    indexed_names = cap_names_raw()


    # Agrega los nodos (números - nombres de autores)
    def populate_graph():
        for name in indexed_names:
            graph.add_vertex(name)
        return graph

    def make_graph():
        graph = populate_graph() # Se modifica popr la versión con nombres o números
        
        rel = {}
        # TODO Agregar datos correctos
        for registro_de_colaboracion in generate_graph_data():
            if len(registro_de_colaboracion) == 2:
                print("DENTRO DEL LOOP ")
                print("rel data: ")
                print(rel)
                temp_one_index = indexed_names.index(registro_de_colaboracion[0])
                print(f"Data 1: { temp_one_index}")
                temp_two_index = indexed_names.index(registro_de_colaboracion[1])
                print(f"Data 2:  { temp_two_index}")
                temp_rel = f"{indexed_names[temp_one_index]} - {indexed_names[temp_two_index]}"
                if  temp_rel in rel:
                    print("DENTRO IF 2")
                    rel[temp_rel] += 1
                    graph.add_edge(registro_de_colaboracion[0], registro_de_colaboracion[1], rel[temp_rel])
                else:
                    rel[temp_rel] = 1
        print(rel)
        #graph.add_edge()

        return graph
    return make_graph()


if __name__ == '__main__':
    print(str(create_graph()))
    print("Not main app, run: python3 main_en.py")