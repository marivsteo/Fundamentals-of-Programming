from model.Cookie import Cookie
class CookieService(object):
    
    
    def __init__(self, __repo, __validator):
        self.__repo = __repo
        self.__validator = __validator
    
    def addCookie(self,ident,name,weight):
        cookie = Cookie(ident,name,weight)
        self.__validator.validateCookie(cookie)
        self.__repo.add(cookie)

    
    def getAllCookies(self):
        return self.__repo.getAll()

    
    def getGoodCookies(self,prefix):
        all = self.__repo.getAll()
        rez = [x for x in all if x.get_name().startswith(prefix)]
        rez.sort(key=lambda x:x.get_weight(),reverse=False)
        return rez