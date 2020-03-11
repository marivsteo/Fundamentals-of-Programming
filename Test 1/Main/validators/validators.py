from errors.errors import ValidError

class validator(object):
    
    def __init__(self):
        pass
    
    def validate(self,student):
        errors = ""
        
        if student.get_id() < 0:
            errors += "Invalid id !\n"
            
        if student.get_grade() < 0 or student.get_grade() > 10:
            errors += "Invalid grade !\n"
            
        if student.get_attendance() < 0:
            errors += "Invalid attendance number !\n"
            
        name = student.get_name()
        params = name.split(' ')
        if len(params[0]) < 2 or len(params[0]) < 2:
            errors += "Invalid name format !\n"
        
        if len(errors) > 0:
            raise ValidError(errors) 