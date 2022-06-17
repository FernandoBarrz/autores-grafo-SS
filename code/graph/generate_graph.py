


from traceback import print_tb
from code.graph.graph.graph import Graph

from code.utils.normalize_names import cap_names_raw
from code.utils.generate_collabs_lists import generate_list_of_authors_from_pub
from code.utils.generate_collabs_num import generate_collabs_num


def generate_graph_data():
    """
    Genera una lista de listas que representan las colaboraciones entre autores
    cada una de las listas internas representa una colaboración entre esos autores.
    """
    # TODO: Hasta este punto estan las colaboraciones en al forma:
    # TODO: [[autor_1_pub, autor_2_pub_1], [autor_1_pub_2, autor_2_pub_2]]

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
    
    #indexed_names = ['clara ines espitia pinzon', 'gloria soberon chavez']
    #TODO: indexed_names = cap_names_raw()
    indexed_names = cap_names_raw()

    print("REGISTRO DE NOMBRES: ", indexed_names)
    # Agrega los nodos (números - nombres de autores)
    def populate_graph():
        for name in indexed_names:
            print(f"{name} -> added to the graph info")
            graph.add_vertex(name)
        return graph

    def make_graph():
        graph = populate_graph() # Se modifica popr la versión con nombres o números
        
        rel = {}
        # TODO Agregar datos correctos
        for registro_de_colaboracion in generate_graph_data(): # TODO: remove slicing
            if len(registro_de_colaboracion) == 1:
                print(f"Eliminado: {registro_de_colaboracion}")
                continue

            if len(registro_de_colaboracion) == 2: # When the collaboration contains only TWO autors
                print("DENTRO DEL LOOP ")
                print("rel data: ")
                print(rel)
                try:
                    temp_one_index = indexed_names.index(registro_de_colaboracion[0])
                    
                    print(f"Data 1: { temp_one_index}")
                    temp_two_index = indexed_names.index(registro_de_colaboracion[1])
                    print(f"Data 2:  { temp_two_index}")
                    temp_rel = f"{indexed_names[temp_one_index]} - {indexed_names[temp_two_index]}"
                    temp_rel_2 = f"{indexed_names[temp_two_index]} - {indexed_names[temp_one_index]}"
                except:
                    print("El registro no esta en las listas de nombres")
                if  temp_rel in rel or temp_rel_2 in rel:
                    print("DENTRO IF 2")
                    #TODO: Remueve el edge con los datos actualez y despues lo vuelve a crear
                    try:

                        graph.remove_edge(indexed_names[temp_one_index], indexed_names[temp_two_index], rel[temp_rel])
                    except Exception:
                        graph.remove_edge(indexed_names[temp_two_index], indexed_names[temp_one_index], rel[temp_rel_2])
                    rel[temp_rel] += 1
                    graph.add_edge(indexed_names[temp_one_index], indexed_names[temp_two_index], rel[temp_rel])
                else:
                    # Actualmente, solo genera una relacion unidireccional de maximo 1, en ocaciones deben de ser 2 o más
                    # TODO: Ocurre que se genera solo una relacion, pero despues no de puede actualizar
                    # TODO: Se debe intenar generar el número de colaboraciones antes de enviarlo al .add_edge()
                    rel[temp_rel] = 1
                    rel[temp_rel_2] = 1
                    graph.add_edge(indexed_names[temp_one_index], indexed_names[temp_two_index], rel[temp_rel])
                
            else:
                print("A greater relation is required")
        print(rel)
        #graph.add_edge()

        return graph
    return make_graph()


if __name__ == '__main__':
    print(str(create_graph()))
    print("Not main app, run: python3 main_en.py")