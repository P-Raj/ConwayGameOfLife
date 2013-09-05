"""Makes complete game graph for a given board of row*column size"""""

import itertools
from pprint import pprint 
import networkx as nx
from sets import Set

import GraphFile

Board = {}
Board["Rows"] = 3
Board["Columns"] = 3


StartStates = []
StatesOfLen = {}

Graph = {}
Cells = []
States = {}
NXGraph = None

def NetworkxGraph():

    global NXGraph
    global Graph
    global States

    NXGraph = nx.DiGraph()
    
    print "Generating networkx graph"
    
    for node in Graph:
        NXGraph.add_node(States[node])
    
    for node in Graph:
        for edge in Graph[node]:
            NXGraph.add_edge(States[node],States[edge[1]])

    print "Created networkx graph"

def Loop():

    global NXGraph
    print "Looking for loops"
    Cycles = nx.simple_cycles(NXGraph)
    print "Cycles:"
    for cycle in Cycles:
        print cycle

def NodeWithNEdges( N ):

    Nodes = []
    for node in Graph:
        if len(Graph[node]) == N:
            Nodes.append(node)
    return Nodes

def WinningNodes():

    Nodes = []
    for node in Graph:
        for edge in Graph[node]:
            if len(edge[1]) == 0:
                Nodes.append(node)
    return Nodes

def NodesWithNAliveNodes( N ):

    Nodes = []
    for node in Graph:
        if len(node) == N:
            Nodes.append(node)
    return Nodes
    
def GenerateCells():

    global Board
    global Cells
    if Cells != []:
        return Cells
    Rows = Board["Rows"]
    Columns = Board["Columns"]

    for row in range(Rows):
        for column in range(Columns):
            Cells.append((row,column))
    
def GetCombinations(Length):

    global Cells

    GenerateCells()
    return itertools.combinations(Cells, Length)

def CBoard(State):
    
    global Board
    
    Rows = Board["Rows"]
    Columns = Board["Columns"]
    CurrentBoard = []
    
    for row in range(Rows):
        
        irow= []
        
        for column in range(Columns):
            
            if (row,column) in State: irow.append(1)
            else: irow.append(0)
            
        CurrentBoard.append(irow)
        
    return CurrentBoard

def AliveNeighbours(CBoard , row , column):

    global Board
    alive = 0
    MaxRows = Board["Rows"]
    MaxColumns = Board["Columns"]
    
    if CBoard[row][column] == 1: alive = -1
    
    for irow in range(max(0,row-1), min(row+2,MaxRows)):
        for icolumn in range(max(0,column-1) , min(column+2,MaxColumns)):
            if CBoard[irow][icolumn] == 1 : alive += 1
            
    return alive

def Evolution(State):

    global Board
    
    Rows = Board["Rows"]
    Columns = Board["Columns"]
    
    PvsBoard = CBoard(State)
    NextState = []

    for row in range(Rows):
        for column in range(Columns):
            
            alive = AliveNeighbours(PvsBoard , row , column)

            if PvsBoard[row][column] == 1:
                #if the cell is alive
                if alive == 3 or alive == 2:
                    NextState.append((row,column)) 
            else:
                if alive == 3 :
                    NextState.append((row,column))
                
    return NextState
    
def NextConfig(CurrentState , AddCell):

    if AddCell in CurrentState:
        return None

    CurrentState = list(CurrentState)
    CurrentState.append(AddCell)
    CurrentState = tuple(CurrentState)
    NextState = Evolution(CurrentState)
    
    return NextState

def GenerateGraph():

    global Board
    global Graph

    Graph = {}
    
    for LiveCells in range(0,Board["Rows"]*Board["Columns"]+1):
        
        Configs = GetCombinations(LiveCells)
        
        StatesOfLen[LiveCells] = Configs

        for config in Configs:
            #config = ((0, 0),)
            if LiveCells == Board["Rows"]*Board["Columns"]/2 : StartStates.append(config)
            Graph[config] = []
    #Graph contains the possible configs


    CellsToAdd = []
    #cells you can add

    for irow in range(Board["Rows"]):
        for icolumn in range(Board["Columns"]):
            CellsToAdd.append((irow,icolumn))

    index = 0

    for node in Graph:
        States[node] = index
        index += 1
        if len(node)!=0 :
            for cell in CellsToAdd:
                NextState = NextConfig(node,cell)
                if NextState!=None: Graph[node].append((cell,tuple(NextState)))

def ShortestPaths():

    global NXGraph
    Paths = {}
    return nx.all_pairs_shortest_path_length( NXGraph )
    
def ReachableStates( Node ):

    return [node for node in nx.all_pairs_shortest_path_length( NXGraph )[Node]]

def RemoveNonReachableState ( ReachableStates ):
    
    global Graph
    NewGraph = {}
    for node in Graph :
        if States[node] in ReachableStates:
            NewGraph[node] = []
            for nxtnode in Graph[node]: 

                if States[nxtnode[1]] in ReachableStates:
                    NewGraph[node].append((nxtnode[0], nxtnode[1]))

    Graph = NewGraph

def ReverseGraph (Graph):

    ReverseGraph = {}

    for node in Graph:
        for nnode in Graph[node]:
            ReverseGraph[nnode[1]] = ReverseGraph.get(nnode[1],[]) + [node]

    return ReverseGraph


def minBound ( Config ):

    Config.sort()
    for node in Config:
        x = node[0]
        y = node[1]
        for i in range(0,y+2):



GenerateGraph()
NetworkxGraph()


#print "Final state :" , States[()]

print "Start States" , [States[state] for state in StartStates]

Final_state = States[()]

Reachable_States = []
for StartState in StartStates :
    reachable_states = ReachableStates(States[StartState])
    Reachable_States += reachable_states
    
    if Final_state not in reachable_states:
        print "Final State not reachable from StartState" , States[StartState]



Reachable_States = list(set(Reachable_States))

RG = ReverseGraph(Graph)
fp = open("Nodelength.txt" , "w")
for node in RG:
    a = [str(len(node))]
    min_bound = minBound(node)
    for r in RG[node]: a.append(str(len(r)))
    fp.write(" ".join(a) + "\n")
    
exit()

#print "Reachable States " , Reachable_States

#RemoveNonReachableState(Reachable_States)

#print Graph

Filename = str(Board["Rows"]) + "X" + str(Board["Columns"]) + ".graph"

Save_Graph = {}
for node in Graph:
    Save_Graph[States[node]] = [States[NxtState[1]] for NxtState in Graph[node]]

GraphFile.Write(Filename,Save_Graph)

Filename = str(Board["Rows"]) + "X" + str(Board["Columns"]) + ".state"

State_Graph = {}
for node in Graph:
    State_Graph[States[node]] = [str(node)]

GraphFile.Write(Filename,State_Graph)

for state in StartStates:
    print "PAth length between " , state , " and  " , Final_state , " " ,nx.all_pairs_shortest_path_length( NXGraph )[States[state]][Final_state]





print States[ ((0, 0), (0, 2), (2, 0), (2, 2)) ]
#path lengths 





#print "Total Number of nodes : " , len(Graph.keys())
#print "Total Winning Nodes : " , len(WinningNodes())
#print "Total nodes with 4 liveNodes : ", len(NodesWithNAliveNodes(4))
#print "Total nodes with 5 liveNodes : ", len(NodesWithNAliveNodes(5))