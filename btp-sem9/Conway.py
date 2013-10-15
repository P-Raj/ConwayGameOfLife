""" Module contains class Conway implementing Conway's Game of Life """
from Graph import Graph
import itertools

class Conway(object):
    """ Class for Conway's Game of Life """

    def __init__ (self, row, column):
        self.row = row
        self.column = column
        self.board = None
        self._map = {}
        self._invertmap = {}
        self._counter = 0
        self._connector = []

    def boardify(self, config):
        """initialize the board according to the config """
        temp_board = [[0]*self.row] * self.column
        for cell in config:
            temp_board[cell[0]][cell[1]] = 1
        return temp_board

    def configure(self, init_config) :
        """sets the intial configuration of the board
           init_config should be of form [cell0,cell1...]
             where celli is a tuple of form (rowi,columni)"""
        self.board = self.boardify(init_config)

    @classmethod
    def linearize(cls, aboard):
        """linearizes the board : aboard """
        rboard = []
        for boards in aboard:
            rboard += boards
        return rboard

    def _should_be_alive(self, row, column):
        """ returns whether the cell (row,column) 
        should be alive in the next iteration or not """
        _alive_neighbors = 0
        for irow in range(max(0, row-1),
                    min(self.row, row+2)):
            for icolumn in range(max(0, column-1), min(self.column, column+2)):
                if self.board[irow][icolumn] == 1 :
                    _alive_neighbors += 1
        if self.board[row][column] == 1:
            _alive_neighbors -= 1
        if self.board[row][column] == 1 :
            if _alive_neighbors == 3 or _alive_neighbors == 2 :
                return True
            return False
        else:
            if _alive_neighbors == 3:
                return True
            return False

    def evolve(self) :
        """the board evolves using conway's rules"""
        newboard = [[0]*self.row] * self.column
        for irow in range(self.row):
            for icolumn in range(self.column) :
                if self._should_be_alive(irow, icolumn):
                    newboard[irow][icolumn] = 1
        return newboard

    def make_graph(self):
        """ Creates the game graph and stores it """
        this = Graph()
        self._counter = 0
        self._connector = []
        options = []
        for irow in range(self.row):
            for icolumn in range(self.column):
                options.append((irow, icolumn))
        live_cells = []
        empty_board = [[0] * self.row] * self.column
        for length in range(self.row * self.column+1):
            live_cells += itertools.combinations(options, length)
        for cell in live_cells:
            self.configure(cell)
            self._add_node(self.board)
            new_board = self.evolve()
            self._add_node(new_board)
            if self.board != empty_board :
                self._add_edge(self.board, new_board)
        this.update_vertices(self._map.values())
        this.update_edges(self._connector)
        this.save_graph("this.graph")
        self.write_config("this.config")
        return this

    def _add_node(self, board):
        """ maps board to a unique number """
        _board = self.linearize(board)
        if (tuple(_board) not in self._map):
            self._map[tuple(_board)] = self._counter
            self._invertmap[self._counter] = board
            self._counter += 1

    def _add_edge(self, from_board, to_board):
        """ adds the edge (from_board,to_board) in the local connector """
        from_board = self.linearize(from_board)
        from_conn = self._map[tuple(from_board)]
        to_board = self.linearize(to_board)
        to_conn = self._map[tuple(to_board)]
        if (from_conn, to_conn) not in self._connector :
            self._connector.append((from_conn, to_conn))

    def write_config(self, filename):
        """ function to write the config file """
        fptr = open(filename,'w')        
        for i in self._invertmap:
            fptr.write(str(i))
            for row in self._invertmap[i]:
                fptr.write ("\n" + "\t")
                for element in row:
                    fptr.write(str(element) + " ")
            fptr.write("\n\n")
        fptr.write("\n \t\t Edges \n\n")
        fptr.write("\n".join([str(k) for k in self._connector]))
        fptr.close()


    def _make_board_readable(self):
        """ beautifies the board """
        return "\n".join([" ".join(irow) for irow in self.board])

    def print_board(self):
        """ prints the board """
        print self._make_board_readable()

    def write_board(self, filename):
        """ writes board into a file with name 'filename' """
        open(filename,'w').write(self._make_board_readable)
