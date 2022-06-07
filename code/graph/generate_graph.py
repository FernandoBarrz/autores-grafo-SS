
from random import randint

from code.graph.graph.graph import Graph

from code.utils.normalize_names import cap_names_raw

def create_graph():
    """
    Llama a la clase Graph para asignarle valores
    """
    
    graph = Graph(directed=False) # Graph(directed=false) for undirected graph
    

    indexed_names = cap_names_raw()[:20]

    def generate_random_num():
        length_indexed_names = len(indexed_names) -1
        return randint(0, length_indexed_names)

    def populate_graph():
        for name in indexed_names:
            graph.add_vertex(name)
        return graph

    def make_graph():
        graph = populate_graph()
        for _ in range(len(indexed_names)):
            graph.add_edge(indexed_names[generate_random_num()], indexed_names[generate_random_num()], generate_random_num())
        return graph
    return make_graph()


if __name__ == '__main__':
    print(str(create_graph()))
    print("Not main app, run: python3 main_en.py")