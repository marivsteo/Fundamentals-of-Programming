from errors.Errors import ValidError
class CookieValidator(object):
    
    
    def __init__(self):
        pass

    
    def validateCookie(self,cookie):
        errors =""
        if cookie.get_ident()<0:
            errors+="bad ident!\n"
        if cookie.get_name()=="":
            errors += "bad name!\n"
        if cookie.get_weight()<0 or cookie.get_weight()>100.0:
            errors += "bad weight!\n"
        if len(errors)>0:
            raise ValidError(errors)
    
    
    



