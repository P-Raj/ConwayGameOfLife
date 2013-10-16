""" Modules contains class for GSG """

class GSG (object) :
    """ Class defines function and variables
    for calculating GSG number of a given
    graph """

    def __init__ (self, graph) :
        self.graph = graph
        self.undefined = None
        self.infinity = float("inf")
        self.val_i = 0
        self.val_m = 0
        self.val_l = {}
        self.val_c = {}
        self.undefined_vertices = []
        for node in self.graph.vertices :
            self.val_l[node] = self.undefined
            self.val_c[node] = self.undefined
            self.undefined_vertices.append(node)

    def condition_satisfied (self, node, i) :
        """ returns whether the GSG condition has been satisfied or not """
        valid_options = []
        for nnode in self.graph.next_nodes(node):
            if self.val_l[nnode] == i :
                return False
            if (self.val_l[nnode] == self.undefined
                or self.val_l[nnode] == self.infinity) :
                valid_options.append(nnode)
        for options in valid_options:
            if i not in self.graph.next_nodes(options) :
                return False
        return True

    def calculate(self) :
        """ calculates the graph values """
        #self.graph
        self.val_i = 0
        while (len(self.undefined_vertices) > 0) :
            cond = True
            while cond:
                cond = False
                for node in self.undefined_vertices:
                    if self.condition_satisfied(node, self.val_i) :
                        cond = True
                        self.undefined_vertices.remove(node)
                        self.val_l[node] = self.val_i
                        self.val_c[node] = self.val_m
                        self.val_m += 1
            for node in self.undefined_vertices:
                if self.val_i not in [self.val_l[n] for n in
                                    self.graph.next_nodes(node)]:
                    self.undefined_vertices.remove(node)
                    self.val_l[node] = self.infinity
                    self.val_c[node] = 0
            self.val_i += 1
        self.graph.save_graph("check")
        self.save("this.value")
        return self.graph.to_dictionary(), self.val_l, self.val_c

    def save(self, filename):
        """ saves the file with 'filename' """
        fptr = open(filename, 'w')
        for node in self.val_l:
            fptr.write(str(node) + " " + str(self.val_l[node]) +
                    " " + str(self.val_c[node]) + "\n")
        fptr.close()
