'''
This is the repository module, where the data will be stored.
'''
from domain.board import board
class repository(object):
    '''
    The repository class will store the data required for the game.
    '''
    def __init__(self):
        self.__elems = []
        self.size = 0

    def initializeBoard(self,board_size):
        first_board = board(board_size)
        self.size = board_size
        self.__elems.append(first_board)
        
    def get_element(self):
        return self.__elems[len(self.__elems) - 1]
    
    def place(self,x,y,turn):
        matrix = self.get_element()
        matrix.place(x,y,turn)
        print(matrix)
        
    def check_full(self):
        matrix = self.get_element()
        return matrix.is_full()
    
    def is_empty(self,x,y):
        matrix = self.get_element()
        return matrix.is_empty(x,y)
    
    def greedy(self):
        matrix = self.get_element()
        return matrix.greedy()