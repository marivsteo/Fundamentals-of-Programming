'''
This is the service module.
'''
from domain.hit import hit
from random import randint
class service(object):
    '''
    This is the service class which will work with the repository and the validator.
    '''
    def __init__(self, repo, valid):
        self.__repo = repo
        self.__valid = valid
    
    def initialize(self,board_size):
        self.__repo.initializeBoard(board_size)

    def get_board(self):
        return self.__repo.get_element()
    
    def place_player(self,x,y,turn):
        new_hit = hit(x,y,self.__repo.size)
        self.__valid.validate_hit(new_hit)
        self.__repo.place(x,y,turn)
        
    def place_ai(self,turn):
        '''
        greedy_matrix = self.__repo.greedy()
        print("\n")
        print(greedy_matrix)
        print("\n")
        '''
        while True:
            x = randint(0,self.__repo.size-1)
            y = randint(0,self.__repo.size-1)
            # print(str(x) + " " + str(y) + " " + str(self.__repo.is_empty(x,y)) + "\n")
            if self.__repo.is_empty(x,y):
                break
        new_hit = hit(x,y,self.__repo.size)
        self.__valid.validate_hit(new_hit)
        self.__repo.place(x,y,turn)
        
    def going(self):
        return self.__repo.check_full()