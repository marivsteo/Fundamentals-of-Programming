class Student(object):
    
    def __init__(self,studId,studName):
        self.__id = studId
        self.__name = studName

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value
        
    def __str__(self):
        return str(self.__id) + ", " + self.__name
    
    id = property(get_id, None, None, None)
    name = property(get_name, set_name, None, None)