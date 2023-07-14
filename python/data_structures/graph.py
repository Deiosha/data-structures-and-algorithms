class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self.graph = {}

    def add_node(self, value):
        new_vertex = Vertex(value)
        if new_vertex not in self.graph:
            self.graph[new_vertex] = []
            return new_vertex

    def size(self):
        return len(self.graph)

    def add_edge(self, node1, node2, weight=0):
        self.add_node(node1)
        self.add_node(node2)

        if node1 != node2:
            self.graph[node1].append([node2, weight])
            self.graph[node2].append([node1, weight])
        else:
            self.graph[node1].append([node2, weight])

    def get_nodes(self):
        return list(self.graph.values())

    def get_neighbors(self, vertex):
        return self.graph[vertex]


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
