class student(object):
    
    def __init__(self,id,name,attendance,grade):
        self.__id = id
        self.__name = name
        self.__attendance = attendance
        self.__grade = grade

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_attendance(self):
        return self.__attendance

    def get_grade(self):
        return self.__grade
    
    def set_grade(self, value):
        self.__grade = value
        
    def __str__(self):
        return str(self.__id) + " " + self.__name + " " + str(self.__attendance) + " " + str(self.__grade)

    def __eq__(self,other):
        return self.get_id() == other.get_id()