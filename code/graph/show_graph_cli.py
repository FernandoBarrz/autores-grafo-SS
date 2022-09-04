from pprint import pprint
from code.graph.generate_graph import create_graph



def show_graph_console():
    """
    Muestra el grafo en su representación como texto
    """
    #create_graph()
    pprint(str(create_graph()))

if __name__ == '__main__':
    show_graph_console()
    print("Not main app, run: python3 main_en.py")