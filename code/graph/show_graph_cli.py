from pprint import pprint

print("Hello there")
try:
    #from code.graph.generate_graph.py import create_graph
    from code.graph.generate_graph import create_graph
except Exception as e:
    print("fawfawfa")


def show_graph_console():
    """
    Muestra el grafo en su representación como texto
    """
    print("Funciona AQUIIIII")
    pprint(str(create_graph()))

if __name__ == '__main__':
    show_graph_console()
    print("Not main app, run: python3 main_en.py")