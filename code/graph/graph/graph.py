#from .edge import Edge
#from code.graph.graph.edge import Edge
#from code.graph.graph.vertex import Vertex
#from .vertex import Vertex


class Edge:
    def __init__(self, start_vertex, end_vertex, weight=1, directed=True):
        self.__start_vertex = start_vertex
        self.__end_vertex = end_vertex
        self.__weight = weight
        self.__directed = directed

    def __str__(self):
        if self.__directed:
            print_pattern = "{0} -{1}-> {2}"
        else:
            print_pattern = "{0} <-{1}-> {2}"
        return print_pattern.format(self.__start_vertex.get_label(), self.__weight, self.__end_vertex.get_label())

    def get_start_vertex(self):
        return self.__start_vertex

    def get_end_vertex(self):
        return self.__end_vertex

    def get_weight(self):
        return self.__weight

    def __lt__(self, other):
        return self.__weight < other.get_weight()

    def __eq__(self, other):
        weight_equal = self.__weight == other.get_weight()
        start_vertex_equal = self.__start_vertex == other.get_start_vertex()
        end_vertex_equal = self.__end_vertex == other.get_end_vertex()

        return weight_equal == start_vertex_equal == end_vertex_equal == True

    def __hash__(self):
        return hash(self.__start_vertex.get_label() +
                    self.__end_vertex.get_label() + str(self.__weight))


class Vertex:
    def __init__(self, label, directed=True):
        self.__label = label
        self.__directed = directed
        self.__edges = set()

    def __str__(self):
        outbound_edges_str = ""
        for edge in self.get_outbound_edges():
            outbound_edges_str += str(edge) + ", "

        inbound_edges_str = ""
        for edge in self.get_inbound_edges():
            inbound_edges_str += str(edge) + ", "

        return "\n\n\nVÉRTICE (nombre): {0}, \nVértices adyacentes (de SALIDA):\n\t {1}\n\t \nVértices adyacentes (de ENTRADA):\n\t {2}\n\t".format(self.__label,
                                                                                outbound_edges_str, inbound_edges_str)

    def get_outbound_edges(self):
        if self.__directed == False:
            return self.__edges

        outbound_edges = []
        for edge in self.__edges:
            if edge.get_start_vertex() == self:
                outbound_edges.append(edge)

        return outbound_edges

    def get_inbound_edges(self):
        if self.__directed == False:
            return self.__edges

        inbound_edges = []
        for edge in self.__edges:
            if edge.get_end_vertex() == self:
                inbound_edges.append(edge)

        return inbound_edges

    def get_edges(self):
        return self.__edges

    def get_label(self):
        return self.__label

    def add_edge(self, edge):
        self.__edges.add(edge)

    def remove_edge(self, edge):
        if edge in self.__edges:
            self.__edges.remove(edge)
        else:
            raise ValueError(
                "Can not find edge {0} in vertex {1}".format(str(edge), str(self)))

    def __eq__(self, other):
        return self.__label == other.get_label()

    def __hash__(self):
        return hash(self.get_label())


class Graph:
    '''
    Generate a Graph class
    '''
    def __init__(self, directed=True):
        self.__vertices = {}
        self.__edges = set()
        self.__directed = directed

    def __str__(self):
        graph_str = ""

        for key in self.__vertices:
            graph_str += str(self.__vertices[key]) + '\n'

        return graph_str

    def add_vertex(self, label):
        if label not in self.__vertices:
            self.__vertices[label] = Vertex(label, self.__directed)

    def add_edge(self, start_label, end_label, weight=1):
        start_vertex = self.get_vertex(start_label)
        end_vertex = self.get_vertex(end_label)

        if (start_vertex or end_vertex) is None:
            raise ValueError("Can not find start or end vertex in graph")

        edge = Edge(start_vertex, end_vertex, weight, self.__directed)

        start_vertex.add_edge(edge)
        if start_vertex != end_vertex:
            end_vertex.add_edge(edge)

        self.__edges.add(edge)

    def remove_edge(self, start_label, end_label, weight=1):
        start_vertex = self.get_vertex(start_label)
        end_vertex = self.get_vertex(end_label)

        if (start_vertex or end_vertex) is None:
            raise ValueError("Can not find start or end vertex in graph")

        edge = Edge(start_vertex, end_vertex, weight, self.__directed)

        if edge not in self.__edges:
            raise ValueError(
                "Can not find edge {0} in graph".format(str(edge)))

        start_vertex.remove_edge(edge)
        end_vertex.remove_edge(edge)
        self.__edges.remove(edge)

    def remove_vertex(self, vertex_label):
        if vertex_label not in self.__vertices:
            raise ValueError(
                "Can not find vertex {0} in graph".format(vertex_label))

        vertex = self.__vertices[vertex_label]

        # remove outbound edges to this vertex for all adjacent vertices
        # make copy of edges in order to avoid RuntimeError : Set changed size during iteration
        inbound_edges_copy = vertex.get_inbound_edges().copy()
        for edge in inbound_edges_copy:
            adjacent_vertex = edge.get_start_vertex()
            adjacent_vertex.remove_edge(edge)

            if edge in self.__edges:
                self.__edges.remove(edge)

        # remove inbound edges from this vertex to all adjacent vertices
        # make copy of edges in order to avoid RuntimeError : Set changed size during iteration
        outbound_edges_copy = vertex.get_outbound_edges().copy()
        for edge in outbound_edges_copy:
            adjacent_vertex = edge.get_end_vertex()
            adjacent_vertex.remove_edge(edge)

            if edge in self.__edges:
                self.__edges.remove(edge)

        # remove vertex from graph
        self.__vertices.pop(vertex_label)

    def get_vertex(self, label):
        return self.__vertices.get(label)

    def get_vertices(self):
        return self.__vertices

    def get_edges(self):
        return self.__edges

    def get_indegree(self, label):
        return len(self.get_vertex(label).get_inbound_edges())

    def get_outdegree(self, label):
        return len(self.get_vertex(label).get_outbound_edges())

    def get_degree(self, label):
        if self.is_directed():
            degree = len(self.get_vertex(label).get_inbound_edges()) + \
                len(self.get_vertex(label).get_outbound_edges())
        else:
            degree = len(self.get_vertex(label).get_outbound_edges())
        return degree

    def is_directed(self):
        return self.__directed


if __name__ == "__main__":
    test_graph = Graph()

    test_graph.add_vertex("a")
    test_graph.add_vertex("b")
    test_graph.add_vertex("c")

    test_graph.add_edge("a", "b", 2)
    test_graph.add_edge("a", "c", 7)
    test_graph.add_edge("c", "b", 1)
    test_graph.add_edge("b", "c", 3)

    test_graph.remove_edge("a", "b", 2)
    test_graph.remove_edge("a", "c", 7)

    test_graph.add_edge("a", "b", 3)
    test_graph.add_edge("a", "c", 30)

    print(test_graph)
    #print(test_graph.__str__())
