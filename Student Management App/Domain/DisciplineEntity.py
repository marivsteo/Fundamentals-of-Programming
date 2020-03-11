class Discipline(object):

    def __init__(self, disciplineId, disciplineName):
        self.__id = disciplineId
        self.__name = disciplineName

    def __str__(self):
        return "Discipline Id: " + str(self.__id) + ", name : " + self.__name

    def __eq__(self, value):
        return self.__id == value.__id

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    id = property(get_id, None, None, None)
    name = property(get_name, set_name, None, None)
