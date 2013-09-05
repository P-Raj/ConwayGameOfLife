from Graph import *
import itertools

class Conway :

	def __init__ (self,row,column):

		self.row = row
		self.column = column
		self.board = None
		self._map = {}
		self._invertmap = {}
		self._counter = 0
		self._connector = []

	def configure(self,initConfig) :

		"""sets the intial configuration of the board 
		   initConfig should be of form [cell0,cell1...] where celli is a tuple of form (rowi,columni)"""

		self.board = [[0]*self.row for i in range(self.column)]

		for cell in initConfig:
			self.board[cell[0]][cell[1]] = 1

	def linearize(self,aboard):

		rboard = []
		for boards in aboard:
			rboard += boards
		return rboard

	def _shouldBeAlive(self,row,column):

		_aliveNeighbors = 0

		for irow in range(max(0,row-1),min(self.row,row+2)):
			for icolumn in range(max(0,column-1), min(self.column,column+2)):
				if self.board[irow][icolumn] == 1 : _aliveNeighbors += 1
		if self.board[row][column] == 1: _aliveNeighbors -= 1

		if self.board[row][column] == 1 :
			if _aliveNeighbors == 3 or _aliveNeighbors == 2 : 
				return True
			return False

		else:
			if _aliveNeighbors == 3: 
				return True
			return False


	def evolve(self) :

		"""the board evolves using conway's rules"""

		newboard = [[0]*self.row for i in range(self.column)]

		for irow in range(self.row):
			for icolumn in range(self.column) :
				if self._shouldBeAlive(irow,icolumn):
					newboard[irow][icolumn] = 1

		return newboard



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
			self._addNode(self.board)
			new_board = self.evolve()
			self._addNode(new_board)
			self._addEdge(self.board,new_board)


		this.updateVertices(self._map.values())
		this.updateEdges(self._connector)
		this.saveGraph("this.graph")
		self.writeConfig("this.config")
		return this

	def _addNode(self, board):

		_board = self.linearize(board)
		if (tuple(_board) not in self._map): 
			self._map[tuple(_board)] = self._counter
			self._invertmap[self._counter] = board
			self._counter +=1

	def _addEdge(self, fromBoard, toBoard):

		fromBoard = self.linearize(fromBoard)
		toBoard = self.linearize(toBoard)
		if (self._map[tuple(fromBoard)],self._map[tuple(toBoard)]) not in self._connector: self._connector.append((self._map[tuple(fromBoard)],self._map[tuple(toBoard)]))

	def writeConfig(self, filename):

		fp = open(filename,'w')
		for i in self._invertmap:
			fp.write(str(i))
			for row in self._invertmap[i]:
				fp.write ("\n" + "\t")
				for element in row:
					fp.write(str(element) + " ")

			fp.write("\n\n")

		fp.write("\n \t\t Edges \n\n")
		fp.write("\n".join([str(k) for k in self._connector]))


	

	def _makeBoardReadable(self):

		return "\n".join([" ".join(irow) for irow in self.board])	

	def printBoard(self):

		print self._makeBoardReadable()

	def writeBoard(self,filename):

		open(filename,'w').write(self._makeBoardReadable)

	
	