class Grade(object):
    
    def __init__(self,id,disciplineId, studId, gradeValue):
        self.__id = id
        self.__disciplineId = disciplineId
        self.__studentId = studId
        self.__value = gradeValue
        self.__student = None

    def __str__(self):
        return "Id = " + str(self.__id) + ", discipline id : " + str(self.__disciplineId) + ", student id : " + str(self.__studentId) + ", grade " + str(self.__value)

    def __eq__(self, value):
        return self.__id == value.__id

    def get_id(self):
        return self.__id

    def get_discipline_id(self):
        return self.__disciplineId

    def get_student_id(self):
        return self.__studentId

    def get_value(self):
        return self.__value

    def set_discipline_id(self, value):
        self.__disciplineId = value
        
    def set_student_id(self,value):
        self.__studentId = value

    def set_value(self, value):
        self.__value = value
        
    def set_student(self,value):
        self.__student = value

    id = property(get_id, None, None, None)
    disciplineId = property(get_discipline_id, set_discipline_id, None, None)
    studentId = property(get_student_id, None, None, None)
    value = property(get_value, set_value, None, None)