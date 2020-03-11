class Cookie(object):
    
    
    def __init__(self, __ident, __name, __weight):
        self.__ident = __ident
        self.__name = __name
        self.__weight = __weight

    def __str__(self):
        return str(self.__ident)+" "+self.__name+" "+str(self.__weight)


    def __eq__(self, value):
        return self.__ident==value.__ident


    def get_ident(self):
        return self.__ident


    def get_name(self):
        return self.__name


    def get_weight(self):
        return self.__weight


    def set_name(self, value):
        self.__name = value


    def set_weight(self, value):
        self.__weight = value

    ident = property(get_ident, None, None, None)
    name = property(get_name, set_name, None, None)
    weight = property(get_weight, set_weight, None, None)
    
    



