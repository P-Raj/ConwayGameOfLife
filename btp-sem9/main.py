#main file
from Graph import *
from GSG import *
from Conway import *
from Conwayvariant import *

def main(loadFilename):

	graph = Graph()
	graph.loadGraph(loadFilename)
	gsg = GSG(graph)
	gsg.Calculate()

def main():

	conway = ConwayVariant(2,2)
	graph = conway.makeGraph()
	gsg = GSG(graph)
	gsg.Calculate()
	print "Task Complete"

if __name__ == "__main__" : 
	main()