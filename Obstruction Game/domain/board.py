'''
This is the board entity module. Here is defined the object board.
'''
class board(object):
    
    def __init__(self,board_size):
        self.__size   = board_size
        self.__matrix = [[]]
        self.initialize_elements()
    
    def initialize_elements(self):
        new_matrix = [ [ ' ' for i in range(self.__size) ] for j in range(self.__size) ]
        self.__matrix = new_matrix

    def get_size(self):
        return self.__size

    def get_matrix(self):
        matrix = []
        for i in range(self.__size):
            row = []
            for j in range(self.__size):
                row.append(self.__matrix[i][j])
            matrix.append(row)
        return matrix

    def set_size(self, value):
        self.__size = value
        
    def place(self,x,y,value):
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if i >= 0 and j >= 0 and i < self.__size and j < self.__size:
                    if value == 8:
                        self.__matrix[i][j] = "X"
                    else:
                        self.__matrix[i][j] = "O"
                        
    def is_full(self):
        value = False
        matrix = self.get_matrix()
        for i in range(0,self.__size):
            for j in range(0,self.__size):
                if matrix[i][j] == " ":
                    value = True
        return value
    
    def is_empty(self,x,y):
        matrix = self.get_matrix()
        if matrix[x][y] == " ":
            return True
        else:
            return False
        
    def is_inside(self,x,y):
        return x >= 0 and y >= 0 and x < self.__size and y < self.__size
        
    def greedy(self):
        matrix = self.get_matrix()
        count_matrix = self.get_matrix()
        dir_i = [-1,-1,-1, 0, 0, 0, 1, 1, 1]
        dir_j = [-1, 0, 1,-1, 0, 1,-1, 0, 1]
        for i in range(0,self.__size):
            for j in range(0,self.__size):
                counter = 0
                for k in range(0,9):
                    new_i = i + dir_i[k]
                    new_j = j + dir_j[k]
                    if self.is_inside(new_i,new_j):
                        if matrix[new_i][new_j] == " ":
                            counter += 1
                count_matrix[i][j] = counter
        return count_matrix
                  
    def __str__(self):
        string = "+---"
        for i in range(0,self.__size):
            string += "+---"
        string += "+\n|   "
        for i in range(0,self.__size):
            string += "| " + str(i) + " "
        string += "|\n"
        string += "+---+---"
        for i in range(1,self.__size):
            string += "+---"
        string += "+"
        string += "\n"
        for i in range(0,self.__size):
            string += "| " + str(i) + " | "
            for j in range(0,self.__size):
                string += str(self.__matrix[i][j])
                string += " | "
            string += "\n"
            string += "+---+---"
            for i in range(1,self.__size):
                string += "+---"
            string += "+"
            string += "\n"
        return string