#main file
from Graph import *
from GSG import *
from Conway import *

def main(loadFilename):

	graph = Graph()
	graph.loadGraph(loadFilename)
	gsg = GSG(graph)
	gsg.Calculate()

def main():

	conway = Conway(3,3)
	graph = conway.makeGraph()
	gsg = GSG(graph)
	gsg.Calculate()
	print "Task Complete"



if __name__ == "__main__" : 
	main()


