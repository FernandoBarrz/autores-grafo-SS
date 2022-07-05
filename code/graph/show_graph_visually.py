from code.graph.graph.graph_visualizer import display_graph
from code.graph.generate_graph import create_graph

def show_graph_image():
    display_graph(create_graph(), "Grafo de colaboraciones (soporta 2 y 3 colaboraciones)")



if __name__ == '__main__':
    print("Not main app, run: python3 main_en.py")