from errors.error import ValidError

class validator(object):
    
    def __init__(self):
        pass
    
    def validate_hit(self,hit):
        error = ""
        
        print(str(hit.get_x()) + " " + str(hit.get_y()))
    
        if hit.get_x() >= 0 and hit.get_y() >= 0 and hit.get_x() < hit.get_max() and hit.get_y() < hit.get_max():
            error = "Valid hit !"
        
        if error == "":
            raise ValidError("Invalid coordinates for the hit !")
        else:
            return error    