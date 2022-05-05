from pprint import pprint
#from graph import *

from graph import Graph
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


from graph.graph_visualizer import display_graph
display_graph(graph, "Prueba 2")

#pprint(str(graph))

