
from code.graph.generate_graph import create_graph
from code.graph.graph.graph import Graph
# from code.graph.graph.graph import Vertex
# from code.graph.graph.graph import Graph

# * {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

temp_graph = create_graph()

def get_vertex_weight(author_name):

    vertex = temp_graph.get_vertex(author_name)
    outbound_edges = vertex.get_outbound_edges()
    
    total_weight = 0

    for edge in outbound_edges:
        total_weight += edge.get_weight()

    return total_weight
        
def sort_nodes_by_num_of_collabs():
    author_x_num_collabs = {}

    with open("./input/nombre-investigadores.txt") as aut_names:
        for line in aut_names.readlines():
            author_name = str(line).strip()
            author_x_num_collabs[author_name] = get_vertex_weight(author_name)
    for k, v in sorted(author_x_num_collabs.items(), key=lambda item: item[1]):        
        print(f"\nNombre: {k} --> Colaboraciones en registradas: {v}\n")


def show_statistics_cli():
    sort_nodes_by_num_of_collabs()




if __name__ == '__main__':
    print("Not main app, run: python3 main_en.py")