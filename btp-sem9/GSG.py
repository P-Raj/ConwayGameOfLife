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

		validOptions = []

		for nnode in self.Graph.nextNodes(node):
			if self.l[nnode] == i:return False
			if self.l[nnode] == self.Undefined or self.l[nnode] == self.Inifinity: validOptions.append(nnode)
		for options in validOptions:

			if i not in self.Graph.nextNodes(options): return False

		return True		

	def Calculate(self) :

		self.i = 0

		
		while (len(self.UndefinedVertices) > 0) :

			cond = True

			while cond:

				cond = False
			
				for node in self.UndefinedVertices:
			
					if self.ConditionSatisfied(node,self.i) :
			
						cond = True
						self.UndefinedVertices.remove(node)
						self.l[node] = self.i
						self.c[node] = self.m
						self.m += 1

			for node in self.UndefinedVertices:
			
				if self.i not in self.Graph.nextNodes(node): 
			
					self.UndefinedVertices.remove(node)
					self.l[node] = self.Inifinity
					self.c[node] = 0

			self.i += 1
		self.save("this.value")
	
	def save(self,filename):

		fp = open(filename,'w')
		for node in self.l:
			fp.write(str(node) + " " + str(self.l[node]) + " " + str(self.c[node]) + "\n")
		fp.close()