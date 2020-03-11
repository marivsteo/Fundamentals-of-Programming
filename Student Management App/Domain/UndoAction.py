class Operation(object):
    
    def __init__(self, function, elem, redo_function, redo_elem, entity):
        self.__undo_function = function
        self.__undo_elem = elem
        self.__redo_function = redo_function
        self.__redo_elem = redo_elem
        self.__entity = entity

    def get_entity(self):
        return self.__entity
    
    def get_redo_function(self):
        return self.__redo_function

    def get_redo_elem(self):
        return self.__redo_elem

    def get_undo_elem(self):
        return self.__undo_elem

    def get_undo_function(self):
        return self.__undo_function
    
    undo_elem = property(get_undo_elem, None, None, None)
    redo_function = property(get_redo_function, None, None, None)
    redo_elem = property(get_redo_elem, None, None, None)
    entity = property(get_entity, None, None, None)
    
class CascadeOperation(object):
    
    def __init__(self):
        self.__operations = [] 
    
    def getAll(self):
        return self.__operations
    
    def add(self, operation):
        self.__operations.append(operation)    