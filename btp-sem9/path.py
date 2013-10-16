import random

MAX_DEPTH = 100
INF = float('inf')

def is_better(option_a, option_b, g_val, h_val):
    if g_val[option_b] == g_val[option_a] and g_val[option_a] == 0 :
        if h_val[option_b] < h_val[option_a]:
            return True
        else:
            return False
    elif g_val[option_b] == 0:
        return True
    elif g_val[option_a] == 0:
        return False
    elif g_val[option_b] == g_val[option_a] and g_val[option_a] == INF :
        if random.random() < 0.5:
            return True
        return False
    elif g_val[option_b] == INF:
        return True
    elif g_val[option_a] == INF:
        return False
    else:
        if random.random() < 0.5:
            return True
        return False



def find_winning_path(graph, start_node, g_val, h_val):


    path = [start_node]

    loosing_option = {}

    for node_index in range(MAX_DEPTH):
        
        if node_index >= len(path):
            print "MAX_DEPTH reached"
            break
        
        node = path[node_index]
        
        if node not in graph: return path

        next_nodes = graph[node]
        
        if len(next_nodes) == 0: return path

        loosing_choice = []
        choice = next_nodes[0]

        if g_val[choice] > 0 :
        	loosing_choice.append(choice)

        for next_node_index in range(1, len(next_nodes)):
            
            if is_better(choice, next_nodes[next_node_index], 
            	g_val, h_val):
                choice = next_nodes[next_node_index]

            if g_val[next_nodes[next_node_index]] > 0 :
            	loosing_choice.append(next_nodes[next_node_index])

        loosing_option[node] = loosing_choice

        if choice not in path:	path.append(choice)
        else: 
        	print "LOOP found @ ", choice
        	break

    return path , loosing_option

#print find_winning_path({'A':['A','B' ,'C'] },'A',{'A':1, 'B':0 ,'C' : 0}, {'A': 0, 'B': 1 , 'C' : 0})