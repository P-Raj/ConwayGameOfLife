from Conway import *
from Graph import *
import itertools

class ConwayVariant(Conway):

	def __init__ (self,row,column) :
		super(ConwayVariant,self).__init__(row,column)

	def findBaseConf(self, conf) :

		baseConfs = []
		for node in conf:
			copyConf = list(conf) + []
			copyConf.remove(node)
			baseConfs.append(self.boardify(copyConf))
		return baseConfs

	def makeGraph(self):

		this = Graph()
		self._counter = 0
		self._connector = []

		options = []
		for irow in range(self.row):
			for icolumn in range(self.column):
				options.append((irow,icolumn))

		liveCells = []

		for length in range(self.row*self.column+1):
			liveCells += itertools.combinations(options,length)

		for cell in liveCells:
			self.configure(cell)
			new_board = self.evolve()
			self._addNode(self.board)
			self._addNode(new_board)
			for confs in self.findBaseConf(cell):
				self._addNode(confs)
				self._addEdge(confs,new_board)


		this.updateVertices(self._map.values())
		this.updateEdges(self._connector)
		this.saveGraph("this.graph")
		self.writeConfig("this.config")
		return this
