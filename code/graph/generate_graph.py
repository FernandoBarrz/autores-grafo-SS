from pprint import pprint
#from graph import *

from code.graph.graph import Graph

def create_graph():
    graph = Graph(directed=False) # Graph(directed=false) for undirected graph

    graph.add_vertex("Pablo")
    graph.add_vertex("Juan")
    graph.add_vertex("Pedro")
    graph.add_vertex("Federica")
    graph.add_vertex("unai")


    graph.add_edge("Pablo", "Juan", 1)
    graph.add_edge("Pedro", "Pablo", 12)
    graph.add_edge("Federica", "unai", 2)
    graph.add_edge("unai", "Pablo", 2)
    graph.add_edge("Juan", "Pedro", 4)
    graph.add_edge("unai", "Pablo", 11)

    return graph


if __name__ == '__main__':
    
    print("Not main app, run: python3 main_en.py")