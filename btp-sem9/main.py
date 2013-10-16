"""         main file        """

from Graph import Graph
from GSG import GSG
from Conwayvariant import ConwayVariant
import path
import player

def main(load_filename):
    graph = Graph()
    graph.load_graph(load_filename)
    gsg = GSG(graph)
    gsg.calculate()
    print "Done"

def main():

    conway = ConwayVariant(3,3)
    gsg = GSG(conway.make_graph())
    a, b, c = gsg.calculate()

    #init_state can either be the actual config or the index of
    #the state in the graph calculated above
    #init_state = 24
    init_state = [[0,1,1],[0,1,0],[1,1,1]]

    if type(init_state) == list:
        init_state = conway.get_state_index(init_state)

    seq = path.find_winning_path(a, init_state, b, c)
    print seq[0]
    conway.print_sequence(seq[0],seq[1])
    #return conway

def game():
    
    init_config = [[0,0,0],[1,1,1],[0,0,0]]
    player.player(init_config)
    
if __name__ == "__main__" :
    print game()
