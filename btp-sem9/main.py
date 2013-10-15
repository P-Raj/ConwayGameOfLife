"""         main file        """

from Graph import Graph
from GSG import GSG
from Conwayvariant import ConwayVariant

def main(load_filename):
    graph = Graph()
    graph.load_graph(load_filename)
    gsg = GSG(graph)
    gsg.calculate()
    print "Done"

def main():
    conway = ConwayVariant(3, 3)
    return conway

if __name__ == "__main__" :
    print main()
