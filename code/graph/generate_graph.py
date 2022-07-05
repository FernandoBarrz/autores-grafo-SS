

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
    # TODO: [[autor_1_pub, autor_2_pub_1], [autor_1_pub_2, ... ,autor_2_pub_2], [autor_N_pub_N, autor_N_pub_N, autor_N_pub_N, ..]]

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

    
    # Agrega los nodos (números o nombres de autores)
    def populate_graph():
        for name in indexed_names:
            graph.add_vertex(name)
        return graph

    def make_graph():
        graph = populate_graph() # Se modifica popr la versión con nombres o números
        rel = {}

        # TODO Probar si aún funciona la forma grafica despues del ultimo cambio

        # TODO Agregar datos para las colaboraciones entre más de 2 autores
        for registro_de_colaboracion in generate_graph_data():
            if len(registro_de_colaboracion) == 1:
                continue

            elif len(registro_de_colaboracion) == 2: # When the collaboration contains only TWO autors

                try:
                    # En una relación de 2 autores, pueden llegar en diferente order
                    temp_one_index = indexed_names.index(registro_de_colaboracion[0])
                    temp_two_index = indexed_names.index(registro_de_colaboracion[1])

                    nombre_autor_1 = indexed_names[temp_one_index]
                    nombre_autor_2 = indexed_names[temp_two_index]

                    # Swap the order of the indices
                    temp_rel = f"{nombre_autor_1} - {nombre_autor_2}"
                    temp_rel_2 = f"{nombre_autor_2} - {nombre_autor_1}"
                except:
                    print("El registro no esta en las listas de nombres")
                if  temp_rel in rel and temp_rel_2 in rel:
                    
                    # Remueve el edge con los datos actualez y despues lo vuelve a crear
                    try:

                        graph.remove_edge(nombre_autor_1, nombre_autor_2, rel[temp_rel])

                    except Exception as error_parte_collbs_2:
                        # Los autores pueden estar en diferentes posiciones en la lista de colaboración
                        # Por ello, se elimina de la siguieente forma, fin antes haber agregado de la misma forma
                        
                        graph.remove_edge(nombre_autor_2, nombre_autor_1, rel[temp_rel_2])

                    rel[temp_rel] += 1
                    rel[temp_rel_2] += 1
                    graph.add_edge(nombre_autor_1, nombre_autor_2, rel[temp_rel])
                else:
                    rel[temp_rel] = 1
                    rel[temp_rel_2] = 1
                    graph.add_edge(nombre_autor_1, nombre_autor_2, rel[temp_rel])
                    # TODO NO Touch

            elif len(registro_de_colaboracion) == 3: # When the collaboration contains only Three autors
                
                # TODO ->  ["pedro", "Juan", "paco"]

                # Autor names come in dynamic position 
                temp_one_index = indexed_names.index(registro_de_colaboracion[0])
                temp_two_index = indexed_names.index(registro_de_colaboracion[1])
                temp_three_index = indexed_names.index(registro_de_colaboracion[2]) # Three author in relation
                # TODO ->  ["pedro"[0], "Juan"[1], "paco"[2]]
                # NO end solutiion
                # TODO: ['1 - 2 - 3', '1 - 3 - 2', '2 - 1 - 3', '2 - 3 - 1', '3 - 1 - 2', '3 - 2 - 1']

                nombre_autor_1 = indexed_names[temp_one_index]
                nombre_autor_2 = indexed_names[temp_two_index]
                nombre_autor_3 = indexed_names[temp_three_index]


                temp_rel_1_p1 = f"{nombre_autor_1} - {nombre_autor_2}"
                temp_rel_1_p2 = f"{nombre_autor_1} - {nombre_autor_3}"

                temp_rel_2_p1 = f"{nombre_autor_2} - {nombre_autor_1}"
                temp_rel_2_p2 = f"{nombre_autor_2} - {nombre_autor_3}"

                temp_rel_3_p1 = f"{nombre_autor_3} - {nombre_autor_1}"
                temp_rel_3_p2 = f"{nombre_autor_3} - {nombre_autor_2}"

                #TODO  Relacion 1 con relacion 2  (1 con 2 y 2 con 1)donde (a -> b | b -> a)
                if temp_rel_1_p1 in rel and temp_rel_2_p1 in rel:
                    try:
                        graph.remove_edge(nombre_autor_1, nombre_autor_2, rel[temp_rel_1_p1])
                    except Exception:
                        graph.remove_edge(nombre_autor_2, nombre_autor_1, rel[temp_rel_2_p1])
                        
                    rel[temp_rel_1_p1] += 1
                    rel[temp_rel_2_p1] += 1
                    graph.add_edge(nombre_autor_1, nombre_autor_2, rel[temp_rel_1_p1])
                else:
                    rel[temp_rel_1_p1] = 1
                    rel[temp_rel_2_p1] = 1
                    graph.add_edge(nombre_autor_1, nombre_autor_2, rel[temp_rel_1_p1])

                #TODO  Relacion 1 con relacion 3 (1 con 3 y 3 con 1) donde (a -> b | b -> a)
                if temp_rel_1_p2 in rel and temp_rel_3_p1 in rel:
                    try:
                        graph.remove_edge(nombre_autor_1, nombre_autor_3, rel[temp_rel_1_p2])
                    except Exception:
                        graph.remove_edge(nombre_autor_3, nombre_autor_1, rel[temp_rel_3_p1])
                    
                    rel[temp_rel_1_p2] += 1
                    rel[temp_rel_3_p1] += 1
                    graph.add_edge(nombre_autor_1, nombre_autor_3, rel[temp_rel_1_p2])
                else:
                    rel[temp_rel_1_p2] = 1
                    rel[temp_rel_3_p1] = 1
                    graph.add_edge(nombre_autor_1, nombre_autor_3, rel[temp_rel_1_p2])

                #TODO  Relacion 2 con relacion 3 (2 con 3 y 3 con 2) donde (a -> b | b -> a)
                if temp_rel_2_p2 in rel and temp_rel_3_p2 in rel:
                    try:
                        graph.remove_edge(nombre_autor_2, nombre_autor_3, rel[temp_rel_2_p2])
                    except Exception:
                        # TODO Here is the problemo
                        
                        graph.remove_edge(nombre_autor_3, nombre_autor_2, rel[temp_rel_3_p2])
                        
                        
                    
                    rel[temp_rel_2_p2] += 1
                    rel[temp_rel_3_p2] += 1
                    graph.add_edge(nombre_autor_2, nombre_autor_3, rel[temp_rel_2_p2])
                else:
                    rel[temp_rel_2_p2] = 1
                    rel[temp_rel_3_p2] = 1
                    graph.add_edge(nombre_autor_2, nombre_autor_3, rel[temp_rel_2_p2])


                

                # temp_rel = f"{nombre_autor_1} - {nombre_autor_2} - {nombre_autor_3}"
                # temp_rel_2 = f"{nombre_autor_1} - {nombre_autor_3} - {nombre_autor_2}"

                # temp_rel_3 = f"{nombre_autor_2} - {nombre_autor_1} - {nombre_autor_3}"
                # temp_rel_4 = f"{nombre_autor_2} - {nombre_autor_3} - {nombre_autor_1}"

                # temp_rel_5 = f"{nombre_autor_3} - {nombre_autor_1} - {nombre_autor_2}"
                # temp_rel_6 = f"{nombre_autor_3} - {nombre_autor_2} - {nombre_autor_1}"
                
                # if  temp_rel in rel or temp_rel_2 in rel or temp_rel_3 in rel or temp_rel_4 in rel or temp_rel_5 in rel or temp_rel_6 in rel:
                    
                #     # Remueve el edge con los datos actualez y despues lo vuelve a crear
                #     try:
                #         graph.remove_edge(nombre_autor_1, nombre_autor_2, rel[temp_rel])
                #     except Exception:
                #         # TODO: correguir revisar si se modifico algo a las relaciones con 2 autores: rel[temp_rel_2]
                #         try:
                #             graph.remove_edge(nombre_autor_2, nombre_autor_1, rel[temp_rel_2])
                #         except Exception:
                #             graph.remove_edge(nombre_autor_2, nombre_autor_1, rel[temp_rel_2])
                #     rel[temp_rel] += 1
                #     graph.add_edge(nombre_autor_1, nombre_autor_2, rel[temp_rel])
                
                # else:
                #     # Actualmente, solo genera una relacion unidireccional de maximo 1, en ocaciones deben de ser 2 o más
                    
                #     # TODO: Agregar la forma en la que se agregan y se borran las colaboraciones
                #     # Les da un valor a manera de señal de que ahora esta registrado (Flag)
                #     rel[temp_rel] = 1
                #     rel[temp_rel_2] = 1
                #     rel[temp_rel_3] = 1
                #     rel[temp_rel_4] = 1
                #     rel[temp_rel_5] = 1
                #     rel[temp_rel_6] = 1
                    
                #     graph.add_edge(nombre_autor_1, nombre_autor_2, rel[temp_rel])
                #     graph.add_edge(nombre_autor_1, nombre_autor_3, rel[temp_rel])
                
            
                
                """
                ['1 - 2 - 3 - 4',
                 '1 - 2 - 4 - 3',
                 '1 - 3 - 2 - 4',
                 '1 - 3 - 4 - 2',
                 '1 - 4 - 2 - 3',
                 '1 - 4 - 3 - 2',
                 '2 - 1 - 3 - 4',
                 '2 - 1 - 4 - 3',
                 '2 - 3 - 1 - 4',
                 '2 - 3 - 4 - 1',
                 '2 - 4 - 1 - 3',
                 '2 - 4 - 3 - 1',
                 '3 - 1 - 2 - 4',
                 '3 - 1 - 4 - 2',
                 '3 - 2 - 1 - 4',
                 '3 - 2 - 4 - 1',
                 '3 - 4 - 1 - 2',
                 '3 - 4 - 2 - 1',
                 '4 - 1 - 2 - 3',
                 '4 - 1 - 3 - 2',
                 '4 - 2 - 1 - 3',
                 '4 - 2 - 3 - 1',
                 '4 - 3 - 1 - 2',
                 '4 - 3 - 2 - 1']
                """
            else:
                
                pass
        
        

        return graph
    return make_graph()


if __name__ == '__main__':
    print(str(create_graph()))
    print("Not main app, run: python3 main_en.py")