""" Module contains Graph class representing a graph """

class Graph(object):
    """ Class represents a graph """

    def __init__ (self):
        self.vertices = []
        self.edges = []
        self.adjacency_matrix = []

    def add_vertex(self, vertex):
        """ adds a new vertex to the graph """
        self.vertices.append(vertex)
        self.vertices = list(set(self.vertices))
        self.init_adjacency_matrix()

    def add_edge(self, from_vertex, to_vertex):
        """ adds a new edge (from_vertex,to_vertex) to the graph """
        self.edges.append((from_vertex, to_vertex))
        self.init_adjacency_matrix()

    def init_adjacency_matrix (self):
        """creates the adjacency matrix for the graph """
        self.adjacency_matrix = [[0]*len(self.vertices)] * self.vertices
        for edge in self.edges :
            t_u = edge[0]
            t_v = edge[1]
            self.adjacency_matrix[t_u][t_v] = 1

    def next_nodes(self, node) :
        """ list of nodes next to the 'node' """
        v_s = []
        t_u = node
        index = 0
        for row in self.adjacency_matrix[t_u] :
            if row > 0 :
                v_s.append(index)
            index += 1
        return v_s

    def update_vertices(self, new_vertices):
        """updates the vertex list """
        self.vertices = new_vertices

    def update_edges(self, new_edges):
        """updates the edge list """
        self.edges = new_edges
        self.init_adjacency_matrix()

    def reachable_vertices(self):
        """returns list of reachable vertices """
        _reachable = []
        for t_e in self.edges:
            _reachable.append(t_e[1])
        _reachable = list(set(_reachable))
        return _reachable

    def non_reachable_vertices(self):
        """returns list of non-reachable vertices """
        _reachable = []
        for t_e in self.edges:
            _reachable.append(t_e[1])
        _nonreachable = (set(self.vertices)).difference(set(_reachable))
        return list(_nonreachable)

    def load_graph(self, filename):
        """loads graph from the file 'filename' """
        self.adjacency_matrix = []
        for line in open(filename,'r').readlines():
            self.adjacency_matrix.append([c.strip() for c in line.split(' ')])

    def save_graph(self, filename):
        """saves the graph in the file 'filename' """
        fptr = open(filename,'w')
        lines = [" ".join([str(j) for j in i]) for i in self.adjacency_matrix]
        fptr.write("\n".join(lines))
