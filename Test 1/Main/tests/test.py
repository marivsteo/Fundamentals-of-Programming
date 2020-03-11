from domain.entity import student
from persistance.repository import repository
import unittest

class test(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)    
        
    def testRepoStudent(self):
        self.__repo = repository("Students.txt")
        assert len(self.__repo) == 0
        
    def testRun(self):
        pass
    
    



