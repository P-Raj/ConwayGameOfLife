# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:32:15 2013

@author: Pranav Raj
"""
from Conwayvariant import ConwayVariant
from GSG import GSG
from Conway import Conway
import os, platform

GAME_GRAPH = {}
CONWAY = None
GSG_VAL = ()
ROW_SIZE = -1
COL_SIZE = -1
CONWAY_state = {}

def calculate_gsg(row_size, col_size):
    global ROW_SIZE, COL_SIZE, GSG_VAL, CONWAY, CONWAY_state
    if (ROW_SIZE != row_size or COL_SIZE != col_size):
        ROW_SIZE = row_size
        COL_SIZE = col_size
        CONWAY = ConwayVariant(ROW_SIZE, COL_SIZE)
        GAME_GRAPH = CONWAY.make_graph()
        GSG_VAL = GSG(GAME_GRAPH).calculate()
        CONWAY_state = CONWAY.get_states()
        
        #GSG = (graph, self.val_l, self.val_c) 

def print_position(position):
    global CONWAY, CONWAY_state
    state = CONWAY_state[position]
    print "".join(["_"] * len(state))
    for row in state:
        print row

def player(init_config):
    """ plays optimally and tries to win if there exists a winning
    strategy """
    global GSG_VAL, CONWAY, CONWAY_state
    _row = len(init_config)
    if _row == 0:
        return
    _column = len(init_config[0])
    if _column == 0:
        return
    calculate_gsg(_row, _column)
    graph = GSG_VAL[0]
    val_l = GSG_VAL[1]
    val_c = GSG_VAL[2]
    start_state = CONWAY.get_state_index(init_config)
    
    if (val_l[start_state] == 0):
        print "No winning move exist from this position "
    else:
        print "There exists a non-loosing move from this position"
    
    pos = start_state    
    
    while (True):
        print_position(pos)
        
        n_nodes = graph[pos]

        options = [i for i in n_nodes if val_l[i] == 0]
        if options == [] :
            options = [i for i in n_nodes if val_l[i] == float('inf')]
        min_c_val = float('inf')
        feasible_option = None
        for option in options:
            if val_c[option] < min_c_val:
                min_c_val = val_c[option]
                feasible_option = option
        
        print
        print "Computer plays ... " , feasible_option
        print 

               
        
        pos = feasible_option
        print_position(pos)
        state_pos = CONWAY_state[pos]
        while True:
            row = input("Enter the row:")
            col = input("Enter the col:")
            if state_pos[row][col] == 0:
                state_pos[row][col] = 1
                break
            print "Cell Already ALIVE !!! "

        if "Windows" in platform.platform() : 
            os.system('cls')
        elif "Linux" in platform.platform() :
            os.system("clear")
        else:
            print "Unknown OS"
            exit()
        print_position(CONWAY.get_state_index(state_pos))        
        
        temp = Conway(ROW_SIZE, COL_SIZE)
        temp.board = state_pos
        state_pos = temp.evolve()
        pos = CONWAY.get_state_index(state_pos)
        