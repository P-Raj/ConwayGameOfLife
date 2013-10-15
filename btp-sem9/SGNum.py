"""
This module contains classes for graphs
and GSG (for calculating sprague grundy
number) os the graph
"""

class Graph(object) :

    """ this class denotes a graph"""

    init_list = []

    def __init__ (self) :

        self.vertices = self.init_list
        self.edges = self.init_list
        self.adjacency_matrix = self.init_list

    def add_vertex(self, vertex) :

        """ adds 'vertex' to the list of vertices """

        self.vertices.append(vertex)
        self.vertices = list(set(self.vertices))
        self.init_adjacency_matrix()

    def add_edge(self, from_vertex, to_vertex) :

        """ adds edge (from_vertex,to_vertex) to the list of edges """

        self.edges.append((from_vertex, to_vertex))
        self.init_adjacency_matrix()

    def init_adjacency_matrix (self) :

        """ updates adjacency matrix representation of graph"""

        self.adjacency_matrix = [[0]*len(self.vertices)] * self.vertices

        for edge in self.edges :

            t_u = self.vertices.index(edge[0])
            t_v = self.vertices.index(edge[1])
            self.adjacency_matrix[t_u][t_v] += 1
            self.adjacency_matrix[t_v][t_u] += 1

    def next_nodes(self, node) :

        """ returns list of next nodes """

        v_s = []
        t_u = self.vertices.index(node)
        index = 0
        for row in self.adjacency_matrix[t_u] :
            if row > 0 :
                v_s.append(self.vertices[index])
            index += 1

class GSG(object) :

    """ class for Generalized Sprague Grundy Theorem """

    def __init__ (self, graph) :

        self.graph = graph
        self.undefined = None
        self.infinity = float("inf")
        self.val_i = 0
        self.val_m = 0
        self.val_l = {}
        self.val_c = {}
        self.undefined_vertices = []

        for node in self.graph.V :
            self.val_l[node] = self.undefined
            self.val_c[node] = self.undefined
            self.undefined_vertices.append(node)


    def condition_satisfied (self, node, i) :

        """ checks for the condition in GSG algorithm """

        #no follower of u is labelled i
        for next_node in self.graph.next_nodes(node) :
            if (self.val_l[next_node] == i) :
                return False
            if (self.val_l[next_node] == self.infinity
                or self.val_l[next_node] == self.undefined) :
                if i not in self.graph.next_node(next_node) :
                    return False
        return True

    def calculate(self) :

        """calculates the value"""

        while len(self.undefined_vertices) != 0 :


            self.val_i += 1






