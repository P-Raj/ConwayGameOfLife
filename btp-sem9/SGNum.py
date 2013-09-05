

class Graph :

	def __init__ (self) :

		self.V = []
		self.E = []
		self.AdjacencyMatrix = []

	def AddVertex(self, vertex) :
		
		self.V.append(vertex)
		self.V = list(set(self.V))
		self.InitAdjacencyMatrix()

	def AddEdge(self, fromVertex, toVertex) :

		self.E.append((fromVertex,toVertex))
		self.InitAdjacencyMatrix()

	def InitAdjacencyMatrix (self) :

		self.AdjacencyMatrix = [[0]*len(self.V) for v in self.V]

		for edge in self.E :

			u = self.V.index(edge[0])
			v = self.V.index(edge[1])
			self.AdjacencyMatrix[u][v] += 1
			self.AdjacencyMatrix[v][u] += 1

	def nextNodes(self,node) :

		v_s = []
		u = self.V.index(node)
		index = 0
		for row in self.AdjacencyMatrix[u] :
			if row > 0 :
				v_s.append(self.V[index])
			index += 1

class GSG :

	def __init__ (self,graph) :

		self.Graph = graph
		self.Undefined = None
		self.Inifinity = float("inf")
		self.i = 0
		self.m = 0
		self.l = {}
		self.c = {}
		self.UndefinedVertices = []

		for node in self.Graph.V :
			self.l[node] = self.Undefined
			self.c[node] = self.Undefined
			self.UndefinedVertices.append(node)


	def ConditionSatisfied (self,node,i) :

		#no follower of u is labelled i
		usefulFollowers = []
		for nextNode in self.Graph.nextNodes(node) :
			if (self.l[nextNode] == i) :
				return false
			if (self.l[nextNode] == self.Inifinity or self.l[nextNode] == self.Undefined) :
				if i not in self.Graph.nextNode(nextNode) :
					return false
		return true

	def Calculate(self) :

		while len(self.UndefinedVertices) != 0 :


			self.i += 1











"""
rithm GSG for computing the Generalized Sprague{Grundy function for a
given nite cyclic digraph G = (V; E).
1. (Initialize labels and counter.) Put i 0, m 0, `(u)  for all u 2 V .
2. (Label and counter.) As long as there exists u 2 V such that no follower
of u is labeled i and every follower of u which is either unlabeled or labeled 1
has a follower labeled i, put `(u) i, c(u) m, m m + 1.
3. (1-label.) For every u 2 V which has no follower labeled i, put `(u) 1.
4. (Increase label.) If V 6= ?, put i i + 1 and return to 2; otherwise end.
"""