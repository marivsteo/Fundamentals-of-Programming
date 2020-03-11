'''
Created on Dec 19, 2018
@author: andreas
'''
from domain.entitity import player
from infrastructure.repository import repo
from bussines.service import serv

class test(object):
    '''
    This function tests whether the service, repository and entity work.
    '''
    def __init__(self):
        pass
    
    def testPlayer(self):
        '''
        This function test the class Player.
        '''
        ply = player("Bill",24.34,10,-2)
        assert ply.get_name()  == "Bill"
        assert ply.get_time()  == 24.34
        assert ply.get_wind()  == -2
        assert ply.get_speed() == 10
        assert str(ply) == "Bill,24.34,10,-2"
        
    def testRepo(self):
        '''
        This function tests the repository class and its functionalities.
        '''
        repository = repo("TestFile.txt")
        list = repository.getElements()
        assert len(list) == 3
        
    def testService(self):
        '''
        This function tests the service class and its methods.
        '''
        repository = repo("TestFile.txt")
        service = serv(repository)
        list = service.getPlayers()
        assert len(list) == 3
        
    def runTests(self):
        '''
        This function calls all the test functions defined above.
        '''
        self.testPlayer()
        self.testRepo()
        self.testService()