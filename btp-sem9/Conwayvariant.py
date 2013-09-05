from Conway import *
from Graph import *
import itertools

class Conwayvariant(Conway):

	def __init__ (self) :
		super(B,self).__init__()

	def evolve(self):

		"""the board evolves using impartial conway's rules"""

		self.newboard = [[0]*self.row for i in range(self.column)]

		_aliveCells = []

		for irow in range(self.row):
			for icolumn in range(self.column) :
				if self.board[irow][icolumn] == 1 :_aliveCells.append((irow,icolumn))

		if (_aliveCells == []) : exit()

		#take user input
		index =  input("\n".join([str(i) for i in _aliveCells]))

		cell = _aliveCells[index]

		_aliveCells.remove()
		self.board[cell[0]][cell[1]] = 0 #kill that cell

		for irow in range(self.row):
			for icolumn in range(self.column) :
				if self._shouldBeAlive(irow,icolumn):
					self.newboard[irow][icolumn] = 1

		self.board = self.newboard

	def updateBoard(self, inputBoard):

		self.board = [[0]*self.row for i in range(self.column)]
		

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

		_from = []
		_to = None
		for cell in liveCells:

			self.configure(cell)
			
			_from = self.board
			self._addNode(self.board)
			new_board = self.evolve()
			self._addNode(new_board)
			self._addEdge(self.board,new_board)


		this.updateVertices(self._map.values())
		this.updateEdges(self._connector)
		this.saveGraph("this.graph")
		self.writeConfig("this.config")
		return this


