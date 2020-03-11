from model.Cookie import Cookie
from valid.Validation import CookieValidator
from errors.Errors import ValidError,RepoError
from repo.Repository import Repository
from business.Service import CookieService

class Test(object):
    
    
    def __init__(self):
        self.__ident = 23
        self.__name = "RaisinCookie"
        self.__weight = 0.75
        self.__cookie = Cookie(self.__ident,self.__name,self.__weight)
        self.__validator = CookieValidator()
        self.__badIdent = -23
        self.__badName = ""
        self.__badWeight = -0.75
        self.__badCookie = Cookie(self.__badIdent,self.__badName,self.__badWeight)
        self.__repo = Repository()
        self.__service = CookieService(self.__repo,self.__validator)
    
    def __testModel(self):
        assert self.__cookie.get_ident()== self.__ident
    
    
    def __testValid(self):
        try:
            self.__validator.validateCookie(self.__cookie)
            assert True
        except ValidError:
            assert False
        
        try:
            self.__validator.validateCookie(self.__badCookie)
            assert False
        except ValidError as ve:
            assert str(ve)=="bad ident!\nbad name!\nbad weight!\n"

    
    def __testRepo(self):
        assert len(self.__repo)==0
        self.__repo.add(self.__cookie)
        assert len(self.__repo)==1
        try:
            self.__repo.add(self.__cookie)
            assert False
        except RepoError as re:    
            assert str(re)=="existing elem!"
        keyCookie = Cookie(self.__ident,None,None)
        assert self.__repo.search(keyCookie)==self.__cookie
        try:
            self.__repo.search(self.__badCookie)
            assert False
        except RepoError as re:
            assert str(re)=="inexisting elem!"
        newCookie = Cookie(self.__ident,"LavaCake",23.45)
        self.__repo.update(newCookie)
        all = self.__repo.getAll()
        assert all == [newCookie]
        assert self.__repo.search(keyCookie) == newCookie
        try:
            self.__repo.update(self.__badCookie)
            assert False
        except RepoError as re:
            assert str(re)=="inexisting elem!"
        removeElem = Cookie(self.__ident,None,None)
        self.__repo.remove(removeElem)  
        try:
            self.__repo.remove(removeElem)
            assert False
        except RepoError as re:
            assert str(re)=="inexisting elem!"
        
    
    def __testBusiness(self):
        assert self.__service.getAllCookies()==[]
        self.__service.addCookie(self.__ident,self.__name,self.__weight)
        cookies = self.__service.getAllCookies()
        assert cookies == [self.__cookie]
        cookie0 = Cookie(67,"placintacumere",34)
        cookie1 = Cookie(3,"placintacurabarbar",5.67)
        
        self.__service.addCookie(67,"placintacumere",34)
        self.__service.addCookie(34,"grandmaspie",45.67)
        self.__service.addCookie(14,"americanpie",25.67)
        self.__service.addCookie(3,"placintacurabarbar",5.67)
        goodCookies = self.__service.getGoodCookies("pl")
        for x in goodCookies:
            print(x)
        assert goodCookies ==[cookie1,cookie0]
        
    def runTests(self):
        self.__testModel()
        self.__testValid()
        self.__testRepo()
        self.__testBusiness()
    
    
    
    



