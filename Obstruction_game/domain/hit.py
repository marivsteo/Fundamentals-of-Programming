'''
This is the hit entity module. Here is defined the object hit.
'''
class hit(object):
    
    def __init__(self, x, y, max):
        self.__x = x
        self.__y = y
        self.__max = max

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
    
    def get_max(self):
        return self.__max