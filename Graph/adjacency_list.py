from collections import OrderedDict

class Vertex:
    """
    Represent each vertex in graph
    """

    def __init__(self, vertex):
        """
        For example. Vertex V0 has vertex = "V0"
                                   connected_to = {V1: 7, V5:3}  # where 7 and 3 are weight of edges
        """
        self.vertex = vertex  # vertex is also called node or vertex
        self.connected_to = OrderedDict()  # using OrderDict instead of common dict to keep the keys of dict in order.
                                         # so that it is easier to implement breath first search and depth first search

    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_vertex(self):
        return self.vertex

    def get_weight(self, neighbor):
        return self.connected_to[neighbor]

    def __str__(self):
        return str(self.vertex) + ' connected_to: ' + str([x.vertex for x in self.connected_to])


class Graph:
    """
    To hold the master list of vertices
    """

    def __init__(self):
        self.vertex_dic = OrderedDict()
        self.num_vertices = 0

    def add_vertex(self, vertex):
        self.num_vertices += 1
        new_vertex = Vertex(vertex)
        self.vertex_dic[vertex] = new_vertex
        return new_vertex

    def get_vertex(self, _vertex):
        if _vertex in self.vertex_dic.keys():
            return self.vertex_dic[_vertex]
        else:
            return None

    def add_edge(self, from_vertext, to_vertex, weight=0):
        if from_vertext not in self.vertex_dic.keys():
            nv = self.add_vertex(from_vertext)
        if to_vertex not in self.vertex_dic.keys():
            nv = self.add_vertex(to_vertex)
        self.vertex_dic[from_vertext].add_neighbor(neighbor=self.vertex_dic[to_vertex], weight=weight)

    def get_vertices(self):
        return self.vertex_dic.keys()

    def __iter__(self):
        return iter(self.vertex_dic.values())

    def __contains__(self, _vertex):
        return _vertex in self.vertex_dic.keys()


if __name__ == "__main__":
    graph = Graph()

    for i in range(4):
        graph.add_vertex('V' + str(i))

    print('vertex_dic = ', graph.vertex_dic)
    print('list of vertices = ', graph.vertex_dic.keys())

    graph.add_edge(from_vertext='V0', to_vertex='V1', weight=9)

    for vertext in graph:
        print('vertext in graph:  ', vertext)
        print('coonection in vertext in graph:  ', vertext.get_connections)
