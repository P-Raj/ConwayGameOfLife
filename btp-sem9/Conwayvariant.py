""" Module implementing our variant of CGoL """
from Conway import Conway
from Graph import Graph
import itertools

class ConwayVariant(Conway):
    """ Class implementing our variant of CGoL """

    this = None

    def __init__ (self, row, column) :
        super(ConwayVariant, self).__init__(row, column)

    def find_base_conf(self, conf) :
        """ returns all the configurations by removing
        one node from the configuration """
        base_confs = []
        for node in conf:
            copy_conf = list(conf) + []
            copy_conf.remove(node)
            base_confs.append(self.boardify(copy_conf))
        return base_confs

    def max_size_reachable(self, this) :
        """ prints  all the reachable nodes and  their size """
        for node in this.reachable_vertices():
            print self._invertmap[node]
            print "####################################"

    def make_graph(self):
        this = Graph()
        self._counter = 0
        self._connector = []
        options = []
        for irow in range(self.row):
            for icolumn in range(self.column):
                options.append((irow, icolumn))
        live_cells = []
        for length in range(self.row * self.column+1):
            live_cells += itertools.combinations(options, length)
        for cell in live_cells:
            self.configure(cell)
            new_board = self.evolve()
            self._add_node(new_board)
            for confs in self.find_base_conf(cell):
                self._add_node(confs)
                self._add_edge(confs, new_board)
        this.update_vertices(self._map.values())
        self._connector.remove((0, 0))
        this.update_edges(self._connector)
        this.save_graph("this.graph")
        self.write_config("this.config")
        #self.max_size_reachable(this)
        return this
