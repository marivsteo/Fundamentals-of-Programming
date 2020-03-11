from Domain.DisciplineEntity import Discipline

class ValidError(Exception):
    pass

class validDiscipline(object):
    
    def __init__(self):
        pass

    def validate(self,discipline):
        errors = ""
        if discipline.get_id() < 0:
            errors += "Invalid id !\n"
        if len(errors) > 0:
            raise ValidError(errors)

class validGrade(object):
    
    def __init__(self):
        pass

    def validate(self,grade):
        errors = ""
        if grade.get_id() < 0:
            errors += "Invalid id !\n"
        if grade.get_student_id() < 0:
            errors += "Invalid student id !\n"
        if grade.get_discipline_id() < 0:
            errors += "Invalid discipline id !\n"
        if grade.get_value() < 1 or grade.get_value() > 10:
            errors += "Invalid grade value !\n"
        if len(errors) > 0:
            raise ValidError(errors)

class validStudent(object):
    def __init__(self):
        pass
    
    def validate(self,student):
        errors = ""
        if student.get_id() < 0:
            errors += "Invalid id !\n"
        if len(errors) > 0:
            raise ValidError(errors)