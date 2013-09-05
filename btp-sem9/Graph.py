class Graph:

	def __init__ (self):

		self.V = []
		self.E = []
		self.AdjacencyMatrix = []

	def AddVertex(self, vertex):
		
		self.V.append(vertex)
		self.V = list(set(self.V))
		self.InitAdjacencyMatrix()

	def AddEdge(self, fromVertex, toVertex):

		self.E.append((fromVertex,toVertex))
		self.InitAdjacencyMatrix()

	def InitAdjacencyMatrix (self):

		self.AdjacencyMatrix = [[0]*len(self.V) for v in self.V]

		for edge in self.E :

			u = edge[0]
			v = edge[1]
			self.AdjacencyMatrix[u][v] = 1

	def nextNodes(self,node) :

		v_s = []
		u = node
		index = 0

		for row in self.AdjacencyMatrix[u] :
			if row > 0 : v_s.append(index)
			index += 1

		return v_s

	def updateVertices(self, newVertices):
		self.V = newVertices

	def updateEdges(self, newEdges):
		self.E = newEdges
		self.InitAdjacencyMatrix()

	def loadGraph(self,filename):

		self.AdjacencyMatrix = []
		for line in open(filename,'r').readlines():
			self.AdjacencyMatrix.append([c.strip() for c in line.split(' ')])

	def saveGraph(self,filename):

		open(filename,'w').write("\n".join([" ".join([str(j) for j in i]) for i in self.AdjacencyMatrix]))